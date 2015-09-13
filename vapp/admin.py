# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Category, Assortiment, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ['order', 'id']


class AssortimentAdmin(admin.ModelAdmin):
    fields = ('category', 'name', 'weight', 'weight_units', 'days', 'pcs', 'is_hit', 'is_new', 'is_comingSoon', 'img')
    list_display = ('name', 'category', 'weight', 'weight_units', 'days', 'is_hit', 'is_new', 'is_comingSoon', 'img')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Assortiment, AssortimentAdmin)
admin.site.register(News)
