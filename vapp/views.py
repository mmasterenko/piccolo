from django.shortcuts import render


def main(req):
    return render(req, 'vapp/main.html')
