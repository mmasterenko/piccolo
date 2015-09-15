# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Category, Assortiment, News


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name',)}),
        (u'Необязательные поля', {'fields': ('order',)})
    ]
    list_display = ('name', 'order')
    ordering = ('order', 'id')


class AssortimentAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Обязательные поля', {
            'fields': ('category', 'name', 'weight', 'weight_units', 'days', 'img'),
            'classes': ('wide',)
        }),
        (u'Необязательные поля', {'fields': ('pcs', 'is_hit', 'is_new', 'is_comingSoon')})
    ]
    list_display = ('name', 'category', 'weight', 'weight_units', 'days', 'is_hit', 'is_new', 'is_comingSoon', 'img')


class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('header', 'text', 'date')}),
        (u'Необязательные поля', {'fields': ('url', 'img')}),
        (u'для SEO', {
            'fields': ('title', 'meta_keywords', 'meta_desc'),
            'classes': ('collapse', 'wide')
        })
    ]
    list_display = ('header', 'date', 'url', 'img')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Assortiment, AssortimentAdmin)
admin.site.register(News, NewsAdmin)
