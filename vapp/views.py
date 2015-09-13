# -*- coding: utf-8 -*-

import os
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import FileResponse, HttpResponse
from django.conf import settings
from vapp.models import Category, Assortiment


def main(req):
    cookies = [
            [
                {'img': '/static/pics/mid/pesoch-1.jpg',
                 'name': u'Венето',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,3',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/mid/pesoch-2.jpg',
                 'name': u'Виареджио',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/mid/pesoch-3.jpg',
                 'name': u'Фатимо',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ],
            [
                {'img': '/static/pics/mid/pesoch-4.jpg',
                 'name': u'Рольяно',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,3',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/mid/pesoch-5.jpg',
                 'name': u'Феличе',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/mid/pesoch-6.jpg',
                 'name': u'Полоска',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ]
        ]
    context = {
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
        ]*3,
        'cookies': cookies,
        'categories': [
            {'id': 1, 'name': u'ПЕЧЕНЬЕ СДОБНО-СЛОЕНОЕ'},
            {'id': 2, 'name': u'ПЕЧЕНЬЕ ПЕСОЧНОЕ'},
            {'id': 3, 'name': u'ПЕЧЕНЬЕ СДОБНОЕ ТВОРОЖНОЕ'}
        ]
    }
    return render(req, 'vapp/main.html', context=context)


def news(req):
    return render(req, 'vapp/news.html')


def assortiment(req, page_id='1'):
    cookie_list = Assortiment.objects.filter(category_id=page_id)
    row_length = 3
    cookies, row = [], []
    for cookie in cookie_list:
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

    category_list = Category.objects.order_by('order', 'id')
    categories = [dict(id=c.id, name=c.name) for c in category_list]
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
