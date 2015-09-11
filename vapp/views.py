# -*- coding: utf-8 -*-

import os
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import FileResponse, HttpResponse
from django.conf import settings


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
    if page_id == '1':
        cookies = [
            [
                {'img': '/static/pics/big/sorrento.jpg',
                 'name': u'Сорренто',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,3',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/chertaldo.jpg',
                 'name': u'Чертальдо',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ],
        ]
    if page_id == '3':
        cookies = [
            [
                {'img': '/static/pics/big/tvoroj.jpg',
                 'name': u'Творожное классическое',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,3',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/tvoroj-cuk.jpg',
                 'name': u'Творожное с цукатами',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/tvoroj-cherry.jpg',
                 'name': u'Творожное с вишней',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ]
        ]
    if page_id == '2':
        cookies = [
            [
                {'img': '/static/pics/big/pesoch-1.jpg',
                 'name': u'Венето',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,3',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/pesoch-2.jpg',
                 'name': u'Виареджио',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/pesoch-3.jpg',
                 'name': u'Фатимо',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ],
            [
                {'img': '/static/pics/big/pesoch-4.jpg',
                 'name': u'Рольяно',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,3',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/pesoch-5.jpg',
                 'name': u'Феличе',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/pesoch-6.jpg',
                 'name': u'Полоска',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ],
            [
                {'img': '/static/pics/big/pesoch-7.jpg',
                 'name': u'Курабье',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ]
        ]
    if page_id in ('4',):
        cookies = []
    context = {
        'cookies': cookies,
        'categories': [
            {'id': 1, 'name': u'ПЕЧЕНЬЕ СДОБНО-СЛОЕНОЕ'},
            {'id': 2, 'name': u'ПЕЧЕНЬЕ ПЕСОЧНОЕ'},
            {'id': 3, 'name': u'ПЕЧЕНЬЕ СДОБНОЕ ТВОРОЖНОЕ'}
        ],
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
