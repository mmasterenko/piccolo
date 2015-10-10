from django.contrib import admin
from versilia.admin_site import custom_admin_site
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


custom_admin_site.register(About, AboutAdmin)
custom_admin_site.register(Job, JobAdmin)
custom_admin_site.register(Contact, ContactAdmin)
custom_admin_site.register(Distributor, DistributorAdmin)
custom_admin_site.register(General, GeneralAdmin)
