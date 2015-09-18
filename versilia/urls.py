"""versilia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from vapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.main, name='main'),
    url(r'^news/$', views.news, name='news'),
    url(r'^news/(?P<news_url>.+)/$', views.news, name='news'),

    url(r'^actions/$', views.actions, name='actions'),
    url(r'^actions/(?P<action_url>.+)/$', views.actions, name='actions'),

    url(r'^assortiment/$', views.assortiment, name='assortiment'),
    url(r'^assortiment/([0-9]+)/$', views.assortiment, name='assortiment'),
    url(r'^about/$', views.about, name='about'),
    url(r'^job/$', views.job, name='job'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^distr/$', views.distributor, name='distributor'),
    url(r'^media/(?P<path>images/.+(?:\.jpeg|\.jpg|\.png))$', views.media, name='media'),
    url(r'^api/(?P<cat_id>[0-9]+)/$', views.api, name='api')
]
