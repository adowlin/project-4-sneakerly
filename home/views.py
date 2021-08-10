from django.shortcuts import render


def index(request):
    """ View to return index.html page """
    return render(request, 'home/index.html')
