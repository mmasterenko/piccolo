# -*- coding: utf-8 -*-

from django.shortcuts import render


def main(req):
    return render(req, 'vapp/main.html')


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
            {'id': 3, 'name': u'ПЕЧЕНЬЕ СДОБНОЕ ТВОРОЖНОЕ'},
            {'id': 4, 'name': u'КРУАССАНЫ'}
        ],
        'page_id': int(page_id)
    }
    return render(req, 'vapp/assortiment.html', context=context)


def about(req):
    return render(req, 'vapp/about.html')


def job(req):
    return render(req, 'vapp/job.html')

