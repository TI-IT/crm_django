from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home/home.html')
# from pathlib import Path
# def index(request):
#     text = Path(__file__).resolve().parent.parent.parent / 'templates'
#     return HttpResponse(text)