# -*- coding: utf-8 -*-

from django.db import models


class About(models.Model):
    class Meta:
        verbose_name_plural = u'О НАС'

    def __unicode__(self):
        return '%s' % u'О НАС'
    text = models.TextField(u'Содержание')


class Job(models.Model):
    class Meta:
        verbose_name_plural = u'ВАКАНСИИ'

    def __unicode__(self):
        return '%s' % u'ВАКАНСИИ'
    text = models.TextField(u'Содержание')


class Contact(models.Model):
    class Meta:
        verbose_name_plural = u'КОНТАКТЫ'

    def __unicode__(self):
        return '%s' % u'КОНТАКТЫ'
    text = models.TextField(u'Содержание')


class Distributor(models.Model):
    class Meta:
        verbose_name_plural = u'ПОСТАВЩИКАМ'

    def __unicode__(self):
        return '%s' % u'ПОСТАВЩИКАМ'
    text = models.TextField(u'Содержание')


class General(models.Model):
    class Meta:
        verbose_name_plural = u'ОБЩАЯ ИНФОРМАЦИЯ'

    def __unicode__(self):
        return '%s' % u'ОБЩАЯ ИНФОРМАЦИЯ'
    address = models.CharField(u'Адрес', max_length=60)
    phone = models.CharField(u'Телефон', max_length=20)
    email = models.EmailField(u'E-mail')
