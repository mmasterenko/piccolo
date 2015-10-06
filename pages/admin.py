from django.contrib import admin
from pages.models import About, Contact, Job, Distributor, General


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'phone', 'email', 'address')
    actions = None


class AboutAdmin(admin.ModelAdmin):
    actions = None


class JobAdmin(admin.ModelAdmin):
    actions = None


class ContactAdmin(admin.ModelAdmin):
    actions = None


class DistributorAdmin(admin.ModelAdmin):
    actions = None


admin.site.register(About, AboutAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(General, GeneralAdmin)
