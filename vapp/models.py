# -*- coding: utf-8 -*-

import os
import errno
from django.core.exceptions import SuspiciousFileOperation
from django.core.files import locks
from django.core.files.move import file_move_safe
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from PIL import Image
from django.utils import six
from django.utils.encoding import smart_text


class SlugNullField(models.SlugField):
    description = "SlugField that stores NULL but returns '' "

    def to_python(self, value):

        if value is None:
            return ''
        if isinstance(value, six.string_types):
            return value
        return smart_text(value)

    def get_prep_value(self, value):  # catches value right before sending to db

        value = super(SlugNullField, self).get_prep_value(value)
        if value == '':
            # if Django tries to save an empty string, send the db None (NULL)
            return None
        else:
            # otherwise, just pass the value
            return self.to_python(value)


class MyImgStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        self.width = self.height = self.img_path = None
        try:
            self.width = kwargs.pop('width')
            self.height = kwargs.pop('height')
            self.img_path = kwargs.pop('img_path')
        except KeyError:
            pass
        super(MyImgStorage, self).__init__(*args, **kwargs)

    def get_available_name(self, name, max_length=None):
        """
        Returns a filename
        """
        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)

        while max_length and len(name) > max_length:
            # Truncate file_root if max_length exceeded.
            truncation = len(name) - max_length
            if truncation > 0:
                file_root = file_root[:-truncation]
                # Entire file_root was truncated in attempt to find an available filename.
                if not file_root:
                    raise SuspiciousFileOperation(
                        'Storage can not find an available filename for "%s". '
                        'Please make sure that the corresponding file field '
                        'allows sufficient "max_length".' % name
                    )
                name = os.path.join(dir_name, "%s%s" % (file_root, file_ext))
        return name

    def _save(self, name, content):
        full_path = self.path(name)

        # Create any intermediate directories that do not exist.
        # Note that there is a race between os.path.exists and os.makedirs:
        # if os.makedirs fails with EEXIST, the directory was created
        # concurrently, and we can continue normally. Refs #16082.
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            try:
                if self.directory_permissions_mode is not None:
                    # os.makedirs applies the global umask, so we reset it,
                    # for consistency with file_permissions_mode behavior.
                    old_umask = os.umask(0)
                    try:
                        os.makedirs(directory, self.directory_permissions_mode)
                    finally:
                        os.umask(old_umask)
                else:
                    os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        if not os.path.isdir(directory):
            raise IOError("%s exists and is not a directory." % directory)

        # There's a potential race condition between get_available_name and
        # saving the file; it's possible that two threads might return the
        # same name, at which point all sorts of fun happens. So we need to
        # try to create the file, but if it already exists we have to go back
        # to get_available_name() and try again.

        while True:
            try:
                # This file has a file path that we can move.
                if hasattr(content, 'temporary_file_path'):
                    file_move_safe(content.temporary_file_path(), full_path)

                # This is a normal uploadedfile that we can stream.
                else:
                    # This fun binary flag incantation makes os.open throw an
                    # OSError if the file already exists before we open it.
                    flags = (os.O_WRONLY | os.O_CREAT | os.O_TRUNC |
                             getattr(os, 'O_BINARY', 0))
                    # The current umask value is masked out by os.open!
                    fd = os.open(full_path, flags, 0o666)
                    _file = None
                    try:
                        locks.lock(fd, locks.LOCK_EX)
                        for chunk in content.chunks():
                            if _file is None:
                                mode = 'wb' if isinstance(chunk, bytes) else 'wt'
                                _file = os.fdopen(fd, mode)
                            _file.write(chunk)
                    finally:
                        locks.unlock(fd)
                        if _file is not None:
                            _file.close()
                        else:
                            os.close(fd)
            except OSError as e:
                if e.errno == errno.EEXIST:
                    # Ooops, the file exists. We need a new file name.
                    name = self.get_available_name(name)
                    full_path = self.path(name)
                else:
                    raise
            else:
                # OK, the file save worked. Break out of the loop.
                break

        # this is my code for resize image
        size = self.width, self.height
        _, file_name = os.path.split(full_path)
        size_path = os.path.join(settings.MEDIA_ROOT, self.img_path, file_name)

        im = Image.open(full_path)
        im.thumbnail(size)
        im.save(size_path)

        if self.file_permissions_mode is not None:
            os.chmod(full_path, self.file_permissions_mode)

        name = os.path.join(self.img_path, file_name)

        return name

assort_fs = MyImgStorage(width=360, height=205, img_path='images/middle')
news_fs = MyImgStorage(width=360, height=205, img_path='images/news')
action_fs = MyImgStorage(width=1280, height=491, img_path='images/actions')


class Category(models.Model):
    class Meta:
        verbose_name_plural = u'Категории товара'

    def __unicode__(self):
        return '%s' % self.name
    help_text = u'Позволяет менять порядок следования в меню'
    name = models.CharField(u'Название', max_length=100)
    order = models.PositiveSmallIntegerField(u'Порядок', help_text=help_text, null=True, blank=True, default=99)


class Assortiment(models.Model):
    class Meta:
        verbose_name_plural = u'Товар'

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('assortiment', args=[self.category_id])

    WEIGHT_UNITS = ((u'г', u'г'), (u'кг', u'кг'))

    category = models.ForeignKey(Category, verbose_name=u'Категория')
    name = models.CharField(u'Наименование', max_length=100)
    desc = models.TextField(u'Описание', max_length=200, null=True, blank=True)

    weight = models.DecimalField(u'Вес единицы', max_digits=6, decimal_places=2, default=2.5)
    weight_units = models.CharField(u'Ед изм', max_length=3, choices=WEIGHT_UNITS, default=u'кг')

    pcs = models.DecimalField(u'Единиц в ящике', max_digits=4, decimal_places=1, null=True, blank=True)
    days = models.PositiveSmallIntegerField(u'Дней', default=45)

    is_hit = models.BooleanField(u'Хит', default=False)
    is_new = models.BooleanField(u'Новинка', default=False)
    is_comingSoon = models.BooleanField(u'Скоро в продаже', default=False)

    img_width = models.PositiveSmallIntegerField(null=True, blank=True)
    img_height = models.PositiveSmallIntegerField(null=True, blank=True)
    img = models.ImageField(u'Картинка', upload_to='images/original', default='',
                            width_field='img_width', height_field='img_height', storage=assort_fs)


class News(models.Model):
    class Meta:
        verbose_name_plural = u'Новости'

    def __unicode__(self):
        return '%s' % self.header

    def get_absolute_url(self):
        return reverse('news', args=[self.id])

    header = models.CharField(u'Заголовок', max_length=80)
    text = models.TextField(u'Текст')
    date = models.DateField(u'Дата', default=now)
    uri_help_text = u'URI под которым будет доступна новость. например: /udivitelnaya-novost/'
    url = SlugNullField(u'URI', help_text=uri_help_text, null=True, blank=True, unique=True, max_length=90, default=None)

    img_width = models.PositiveSmallIntegerField(null=True, blank=True)
    img_height = models.PositiveSmallIntegerField(null=True, blank=True)
    help_text = u'Картинка, которая отображается на главной странице'
    img = models.ImageField(u'Картинка', upload_to='images/news', default='', null=True, blank=True,
                            width_field='img_width', height_field='img_height', help_text=help_text, storage=news_fs)
    # for SEO
    meta_keywords = models.CharField('<meta> keywords content', max_length=100, null=True, blank=True)
    meta_desc = models.CharField('<meta> description content', max_length=100, null=True, blank=True)
    title = models.CharField('<title>', max_length=100, null=True, blank=True)


class Actions(models.Model):
    class Meta:
        verbose_name_plural = u'Акции'

    def __unicode__(self):
        return '%s' % self.header

    def get_absolute_url(self):
        return reverse('actions', args=[self.id])

    header = models.CharField(u'Заголовок', max_length=80)
    text = models.TextField(u'Текст')
    date = models.DateField(u'Дата', default=now)
    uri_help_text = u'URI под которым будет доступна акция. например: /novaya-akciya/'
    url = SlugNullField(u'URI', help_text=uri_help_text, null=True, blank=True, unique=True, max_length=90, default=None)

    header_help = u'скрывать заголовок в баннере на главной странице'
    text_help = u'скрывать текст в баннере на главной странице'
    is_hide_header = models.BooleanField(u'Скрыть заголовок в баннере', default=False, help_text=header_help)
    is_hide_text = models.BooleanField(u'Скрыть текст в баннере', default=False, help_text=text_help)

    img_width = models.PositiveSmallIntegerField(u'Ширина (px)', null=True, blank=True)
    img_height = models.PositiveSmallIntegerField(u'Высота (px)', null=True, blank=True)
    help_text = u'ВНИМАНИЕ: убедитесь что картинка соотвествует размерам 1280 x 491'
    img = models.ImageField(u'Картинка', upload_to='images/actions', default='', null=False, blank=True,
                            width_field='img_width', height_field='img_height', help_text=help_text, storage=action_fs)
    # for SEO
    meta_keywords = models.CharField('<meta> keywords content', max_length=100, null=True, blank=True)
    meta_desc = models.CharField('<meta> description content', max_length=100, null=True, blank=True)
    title = models.CharField('<title>', max_length=100, null=True, blank=True)
