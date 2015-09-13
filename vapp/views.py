# -*- coding: utf-8 -*-

import os
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings
from vapp.models import Category, Assortiment


def main(req):
    page_id = '3'
    assortiment_queryset = Assortiment.objects.filter(category_id=page_id)
    cookies, row, row_length = [], [], 3
    for cookie in assortiment_queryset:
        d = {
            'img': cookie.img.url,
            'name': cookie.name,
            'pcs_weight': cookie.weight,
            'weight_units': cookie.weight_units,
            'pcs_per_box': cookie.pcs,
            'shelf_life': cookie.days
        }
        row.append(d)
        if len(row) >= row_length:
            cookies.append(row)
            row = []
    cookies.append(row)

    category_queryset = Category.objects.order_by('order', 'id')
    categories = [dict(id=c.id, name=c.name) for c in category_queryset]

    context = {
        'cookies': cookies,
        'categories': categories,
        'page_id': int(page_id),
        'news': [
            {
                'img': '/static/images/dummy-cake.jpg',
                'header': u'ЗАГОЛОВОК НОВОСТИ',
                'text': u'''
                                Компания “Версилия” – молодое, динамично развивающиеся предприятие,
                                успевшее зарекомендовать себя на рынке кондитерских изделий России как весьма
                                перспективный партнер. Наше предприятие выпускает кондитерские изделия из слоеного,
                                песочного, сдобного и бисквитного теста, а также, пирожные с длительным ...
                            ''',
                'date': u'22 Апреля 11:25',
                'url': reverse(news)
            }
        ]*3
    }
    return render(req, 'vapp/main.html', context=context)


def news(req, news_url=''):
    return render(req, 'vapp/news.html')


def assortiment(req, page_id='1'):
    assortiment_queryset = Assortiment.objects.filter(category_id=page_id)
    cookies, row, row_length = [], [], 3
    for cookie in assortiment_queryset:
        d = {
            'img': cookie.img.url,
            'name': cookie.name,
            'pcs_weight': cookie.weight,
            'weight_units': cookie.weight_units,
            'pcs_per_box': cookie.pcs,
            'shelf_life': cookie.days
        }
        row.append(d)
        if len(row) >= row_length:
            cookies.append(row)
            row = []
    cookies.append(row)

    category_queryset = Category.objects.order_by('order', 'id')
    categories = [dict(id=c.id, name=c.name) for c in category_queryset]

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
