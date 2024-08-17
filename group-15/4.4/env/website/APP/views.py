from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect


 
def index(request):
    return HttpResponse("<h2>Главная</h2>")

def archive(request, year=2021):
    if year > 2023:
        return HttpResponseRedirect('/')
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")

