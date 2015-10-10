# -*- coding: utf-8 -*-

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class CustomAdminSite(AdminSite):
    site_title = u'Версилия'
    site_header = u'Администрирование сайта piccolospb.ru'

custom_admin_site = CustomAdminSite()

custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, GroupAdmin)
