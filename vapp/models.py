# -*- coding: utf-8 -*-

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Assortiment(models.Model):
    UNITS = ((u'г', u'г'), (u'кг', u'кг'))

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    weight = models.PositiveSmallIntegerField()
    weightUnits = models.CharField(max_length=3 ,choices=UNITS)
    pcs = models.DecimalField(max_digits=3, decimal_places=1)
    days = models.PositiveSmallIntegerField()
    isHit = models.BooleanField()
    isNew = models.BooleanField()
    isComingSoon = models.BooleanField()
