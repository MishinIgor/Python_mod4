from django.shortcuts import render
from django.http import JsonResponse, FileResponse, HttpResponseForbidden
from os import listdir
import random
def index(request):
    return render(request, 'index.html')

def cat(request):
    return render(request, 'cat.html')

def dog(request):
    return render(request, 'dog.html')

from django.http import JsonResponse

def json_show(request):
    return JsonResponse({
            'info': {
                'name': 'Petya',
                'lastname': 'Ivanov',
                'age': 16,
            },
            'contacts': {
                'email': 'superpetya@yandex.ru',
                'skype': None,
            },
        })

def picture(request):
    return FileResponse(open(f'APP/static/files/{random.randint(1,3)}.png', 'rb'))