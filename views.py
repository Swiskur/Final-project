from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    context = {"language": ['HTML', 'Python','Django']}
    return render(request, 'index.html', context)


def password(request):

    options = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*')
    generated_password = ''
    for x in range(12):
        generated_password += random.choice(options)


    return render(request, 'password.html', {'password': generated_password})
