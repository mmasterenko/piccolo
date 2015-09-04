from django.shortcuts import render


def main(req):
    return render(req, 'vapp/main.html')


def news(req):
    return render(req, 'vapp/news.html')


def assortiment(req):
    return render(req, 'vapp/assortiment.html')
