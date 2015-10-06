from django.contrib import admin
from django.core.urlresolvers import reverse
from pages.models import About, Contact, Job, Distributor, General


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'phone', 'email', 'address')
    actions = None


class AboutAdmin(admin.ModelAdmin):
    actions = None

    def view_on_site(self, model):
        return reverse('about')


class JobAdmin(admin.ModelAdmin):
    actions = None

    def view_on_site(self, model):
        return reverse('job')


class ContactAdmin(admin.ModelAdmin):
    actions = None

    def view_on_site(self, model):
        return reverse('contact')


class DistributorAdmin(admin.ModelAdmin):
    actions = None

    def view_on_site(self, model):
        return reverse('distributor')


admin.site.register(About, AboutAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(General, GeneralAdmin)
