from django.shortcuts import render
from django.http import JsonResponse, FileResponse, HttpResponseForbidden, HttpResponseNotFound
from os import listdir
import os
def index(request):
    return render(request, 'index.html')

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

def file_show(request, id):
    dir = listdir('APP/files')
    if int(id) > len(dir):
        return HttpResponseForbidden()
    elif int(id) == 0:
        return HttpResponseForbidden()
    else:
        return FileResponse(open('APP/files/{id}.png','rb'))

def download_file(request):
    #Путь к файлу, который вы хотите отправить
    file_path = '/APP/static/text/file.txt'
    
    #Убедитесь, что фаайл существует
    if os.path.exists(file_path):
        #Открываем файл в режиме бинарного чтения
        with open(file_path,'rb') as file:
            #Создаём FileResponse и передаем файл
            response = FileResponse(file)
        #Устанавливаем имя файла, которое будет отображаться при скачивании
        response['Content-Disposition'] = 'attachment'; filename = 'yourfile.txt'
        return response
    else:
        #Если файл не найден, возвращаем ошибку 404
        return HttpResponseNotFound('File not found')

def download_image(request):
    #Путь к изображению
    image_path = '/APP/static/images/1.png'
    
    #Убедитесь, что изображние существует
    if os.path.exists(image_path):
        with open(image_path,'rb') as image:
            #Создаём FileResponse для отправки изображения
            response = FileResponse(image,content_type = 'image/png')
            #Устанавливаем имя файла, которое будет отображаться при скачивании
            response['Content-Disposition'] = 'attachment'; filename = 'yourimage.png'
            return response
    else:
        return HttpResponseNotFound('Image not found')
    
def new_page(request):
    return render(request, 'new_page.html')

def pictures(request):
    return FileResponse(open('APP/files/1.png','rb'))