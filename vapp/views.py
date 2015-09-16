# -*- coding: utf-8 -*-

import os
import json
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings
from vapp.models import Assortiment, News
from vapp.helpers import assortiment_queryset_to_structure, get_categories_list


def main(req):
    categories = get_categories_list()
    news_queryset = News.objects.order_by('-date', 'id')[:3]
    news_list = [{
                     'img': n.img.url if hasattr(n.img, 'url') else '',
                     'header': n.header,
                     'text': n.text,
                     'date': n.date,
                     'url': reverse(news, args=[n.url]) if n.url else reverse(news, args=[n.id])
                 } for n in news_queryset]

    context = {
        'categories': categories,
        'news': news_list
    }
    return render(req, 'vapp/main.html', context=context)


def news(req, news_url=''):
    if not news_url:
        news_object = News.objects.order_by('-date')[0]
    else:
        try:
            selector = int(news_url)
            news_object = News.objects.filter(id=selector)[0]
        except ValueError:
            news_object = News.objects.filter(url=news_url)[0]

    context = {'news':
        {
            'header': news_object.header,
            'text': news_object.text,
            'date': news_object.date,
            'img': news_object.img.url if hasattr(news_object.img, 'url') else ''
        }}

    return render(req, 'vapp/news.html', context=context)


def assortiment(req, page_id=None):
    categories = get_categories_list()
    if not page_id:
        page_id = categories[0].get('id')
    assortiment_queryset = Assortiment.objects.filter(category_id=page_id)
    cookies = assortiment_queryset_to_structure(assortiment_queryset)
    context = {
        'cookies': cookies,
        'categories': categories,
        'page_id': int(page_id)
    }
    return render(req, 'vapp/assortiment.html', context=context)


def about(req):
    return render(req, 'vapp/about.html')


def job(req):
    return render(req, 'vapp/job.html')


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

    assortiment_queryset = Assortiment.objects.filter(category_id=cat_id)[:6]
    cookies = assortiment_queryset_to_structure(assortiment_queryset)
    response = json.dumps(cookies)
    return HttpResponse(response)
