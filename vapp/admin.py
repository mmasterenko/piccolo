from django.contrib import admin
from models import Category, Assortiment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


class AssortimentAdmin(admin.ModelAdmin):
    fields = ('category', 'name', 'weight', 'weight_units', 'days', 'pcs', 'is_hit', 'is_new', 'is_comingSoon', 'img')
    list_display = ('name', 'category', 'weight', 'weight_units', 'days', 'is_hit', 'is_new', 'is_comingSoon', 'img')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Assortiment, AssortimentAdmin)
