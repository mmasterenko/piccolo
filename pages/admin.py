from django.contrib import admin
from pages.models import About, Contact, Job, Distributor, General


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'phone', 'email', 'address')


admin.site.register(About)
admin.site.register(Job)
admin.site.register(Contact)
admin.site.register(Distributor)
admin.site.register(General, GeneralAdmin)
