# -*- coding: utf-8 -*-

import os
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from vapp.models import News, Actions
from pages.models import About, Contact, Distributor, Job
from vapp.helpers import get_assortiment_list, get_categories_list, get_news_url


def main(req):
    categories = get_categories_list()

    actions_queryset = Actions.objects.order_by('-date')[:6]
    action_list = [{
                       'header': a.header,
                       'text': a.text,
                       'img': a.img.url if hasattr(a.img, 'url') else '',
                       'url': reverse('actions', args=[a.url]) if a.url else reverse('actions', args=[a.id]),
                       'is_hide_header': a.is_hide_header,
                       'is_hide_text': a.is_hide_text
                   } for a in actions_queryset]

    news_queryset = News.objects.order_by('-date', 'id')[:3]
    news_list = [{
                     'img': n.img.url if hasattr(n.img, 'url') else '',
                     'header': n.header,
                     'text': n.text,
                     'date': n.date,
                     'url': get_news_url(n)
                 } for n in news_queryset]

    context = {
        'categories': categories,
        'news': news_list,
        'actions': action_list
    }
    return render(req, 'vapp/main.html', context=context)


def news(req, news_url=''):
    context = {}  # default context
    if not news_url:
        return HttpResponseRedirect('/news/pages/1/')
    else:
        try:
            selector = int(news_url)
            news_object = News.objects.filter(id=selector).first()
        except ValueError:
            news_object = News.objects.filter(url=news_url).first()

    if news_object:
        context = {'news':
            {
                'header': news_object.header,
                'text': news_object.text,
                'date': news_object.date,
                'img': news_object.img.url if hasattr(news_object.img, 'url') else '',
                'title': news_object.title,
                'meta_keywords': news_object.meta_keywords,
                'meta_description': news_object.meta_desc
            }}

    return render(req, 'vapp/news.html', context=context)


def news_pages(req, page=None):
    if not page:
        page = 1
    all_news = News.objects.order_by('-date', '-id')
    paginator = Paginator(all_news, 4)
    news_page = paginator.page(page)
    return render(req, 'vapp/news.html', {'news_page': news_page})


def actions(req, action_url=''):
    context = {}  # default context
    if not action_url:
        action = Actions.objects.order_by('-date').first()
    else:
        try:
            selector = int(action_url)
            action = Actions.objects.filter(id=selector).first()
        except ValueError:
            action = Actions.objects.filter(url=action_url).first()

    if action:
        context = {'action':
            {
                'header': action.header,
                'text': action.text,
                'date': action.date,
                'img': action.img.url if hasattr(action.img, 'url') else '',
                'title': action.title,
                'meta_keywords': action.meta_keywords,
                'meta_description': action.meta_desc
            }}

    return render(req, 'vapp/actions.html', context=context)


def assortiment(req, page_id=None):
    categories = get_categories_list()
    if not categories:
        return render(req, 'vapp/assortiment.html')
    if not page_id:
        page_id = categories[0].get('id')
    cookies = get_assortiment_list(page_id)
    context = {
        'cookies': cookies,
        'categories': categories,
        'page_id': int(page_id)
    }
    return render(req, 'vapp/assortiment.html', context=context)


def about(req):
    page = About.objects.first()
    return render(req, 'vapp/about.html', {'page': page})


def job(req):
    page = Job.objects.first()
    return render(req, 'vapp/job.html', {'page': page})


def contact(req):
    page = Contact.objects.first()
    return render(req, 'vapp/contact.html', {'page': page})


def distributor(req):
    page = Distributor.objects.first()
    return render(req, 'vapp/distributor.html', {'page': page})


def media(req, path):
    file_name = os.path.join(settings.MEDIA_ROOT, path)
    _, file_ext = os.path.splitext(file_name)

    content_type = 'image/jpeg'  # default value
    if file_ext.lower() in ('.jpg', '.jpeg'):
        content_type = 'image/jpeg'
    if file_ext.lower() in ('.png',):
        content_type = 'image/png'

    image_data = open(file_name, 'rb').read()
    return HttpResponse(image_data, content_type=content_type)


def api(req, cat_id=''):
    if not cat_id:
        return HttpResponse('no data')

    cookies = get_assortiment_list(cat_id, limit=6)
    response = json.dumps(cookies)
    return HttpResponse(response)
