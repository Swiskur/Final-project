from django.shortcuts import render
from django.http import HttpResponse
from .generator import random_password


def index(request):
    context = {"language": ['HTML', 'Python','Django', 'CSS']}
    return render(request, 'index.html', context)


def password(request):


    return HttpResponse(random_password())
