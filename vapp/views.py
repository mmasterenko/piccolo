from django.shortcuts import render


def main(req):
    return render(req, 'vapp/main.html')


def news(req):
    return render(req, 'vapp/news.html')


def assortiment(req):
    return render(req, 'vapp/assortiment.html')


def about(req):
    return render(req, 'vapp/about.html')


def job(req):
    return render(req, 'vapp/job.html')

