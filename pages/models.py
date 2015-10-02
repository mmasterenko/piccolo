# -*- coding: utf-8 -*-

from django.db import models


class About(models.Model):
    def __unicode__(self):
        return '%s' % u'О НАС'
    text = models.TextField(u'Содержание')


class Job(models.Model):
    def __unicode__(self):
        return '%s' % u'ВАКАНСИИ'
    text = models.TextField(u'Содержание')


class Contact(models.Model):
    def __unicode__(self):
        return '%s' % u'КОНТАКТЫ'
    text = models.TextField(u'Содержание')


class Distributor(models.Model):
    def __unicode__(self):
        return '%s' % u'ПОСТАВЩИКАМ'
    text = models.TextField(u'Содержание')

