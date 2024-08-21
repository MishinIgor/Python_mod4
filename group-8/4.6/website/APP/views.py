from django.shortcuts import render
from django.http import JsonResponse,FileResponse, HttpResponseForbidden
from os import listdir

def index(request):
    return render(request, 'index.html')

def json_show(request):
    return JsonResponse(
        {
            'info': {
                'name': 'Petya',
                'lastname': 'Ivanov',
                'age': 16,
            },
            'contacts': {
                'email': 'superpetya@yandex.ru',
                'skype': None
            },
        }
        )

def file_show(request, id):
    dir = listdir('APP/files')
    if int(id) > len(dir):
        return HttpResponseForbidden()
    elif int(id) == 0:
        return HttpResponseForbidden()
    else:
        return FileResponse(open('APP/files/files/{id}.png', 'rb'))
