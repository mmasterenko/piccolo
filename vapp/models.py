# -*- coding: utf-8 -*-

from django.db import models


class Category(models.Model):
    def __unicode__(self):
        return '%s' % self.name
    help_text = u'Позволяет менять порядок следования в меню. По умолчанию 0 ' \
                u'(в этом случае используется стандартный порядок)'
    name = models.CharField(u'Название', max_length=100)
    order = models.PositiveSmallIntegerField(u'Порядок', default=0, help_text=help_text)


class Assortiment(models.Model):
    def __unicode__(self):
        return '%s' % self.name

    WEIGHT_UNITS = ((u'г', u'г'), (u'кг', u'кг'))

    category = models.ForeignKey(Category, verbose_name=u'Категория')
    name = models.CharField(u'Название', max_length=200)

    weight = models.DecimalField(u'Вес единицы', max_digits=3, decimal_places=1)
    weight_units = models.CharField(u'Ед изм', max_length=3, choices=WEIGHT_UNITS, default=u'кг')

    pcs = models.DecimalField(u'Единиц в ящике', max_digits=3, decimal_places=1, null=True, blank=True)
    days = models.PositiveSmallIntegerField(u'Дней', default=45)

    is_hit = models.BooleanField(u'Хит')
    is_new = models.BooleanField(u'Новинка')
    is_comingSoon = models.BooleanField(u'Скоро в продаже')

    file = models.FileField(u'Файл', default='', upload_to='original')
    img = models.ImageField(u'Картинка', upload_to='img', default='')
