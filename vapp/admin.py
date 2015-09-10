from django.contrib import admin
from models import Category, Assortiment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


class AssortimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'weight', 'weight_units', 'pcs', 'days', 'is_hit', 'is_new', 'is_comingSoon',
                    'file', 'img')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Assortiment, AssortimentAdmin)
