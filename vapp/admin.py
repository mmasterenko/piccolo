# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Category, Assortiment, News, Actions


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name',)}),
        (u'Необязательные поля', {
            'fields': ('order',),
            'classes': ('collapse',)
        })
    ]
    list_display = ('name', 'order')
    ordering = ('order', 'id')


class AssortimentAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Обязательные поля', {
            'fields': ('category', 'name', 'weight', 'weight_units', 'days', 'img'),
            'classes': ('wide',)
        }),
        (u'Необязательные поля', {
            'fields': ('desc', 'pcs', 'is_hit', 'is_new', 'is_comingSoon'),
            'classes': ('wide',)
        })
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


class ActionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('header', 'is_hide_header', 'text', 'is_hide_text', 'date', 'img', 'url')}),
        (u'для SEO', {
            'fields': ('title', 'meta_keywords', 'meta_desc'),
            'classes': ('collapse', 'wide')
        })
    ]
    list_display = ('header', 'date', 'url', 'is_hide_header', 'is_hide_text', 'img')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Assortiment, AssortimentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Actions, ActionsAdmin)
