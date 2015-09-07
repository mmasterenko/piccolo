# -*- coding: utf-8 -*-

from django.shortcuts import render


def main(req):
    return render(req, 'vapp/main.html')


def news(req):
    return render(req, 'vapp/news.html')


def assortiment(req, page_id=1):
    context = {
        'cookies': [
            [
                {'img': '/static/pics/big/sorrento-big.jpg',
                 'name': u'Сорренто',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,3',
                 'shelfLife': u'90 дней'
                 },
                {'img': '/static/pics/big/chertaldo-big.jpg',
                 'name': u'Чертальдо',
                 'pcsWeight': u'1000г',
                 'pcsPerBox': '2,5',
                 'shelfLife': u'90 дней'
                 }
            ],
        ],
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

