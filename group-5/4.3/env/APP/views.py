from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
   return HttpResponse('Hello World')

def game(requset):
    #Генерируем 3 рандомных числа
    num1 = random.randint(0,3)
    num2 = random.randint(0,3)
    num3 = random.randint(0,3)
    
    #Проверка на равенство всех чисел
    if num1 == num2 == num3: 
        response = f'Победа, все 3 числа равны {num1}!'
    else:
        response = f'Повезет в следующий раз! Числа: {num1}, {num2}, {num3}'
    
    return HttpResponse(response)

def rand_hleb(request):
    #Создаём список хлеба и генерируем 3 вариации выбора
    hleb = ['Булка белого', 'Булка чёрного', 'Рисовый парной']
    hleb1 = random.choice(hleb)
    hleb2 = random.choice(hleb)
    hleb3 = random.choice(hleb)
    my_hleb = {}
    #Проверка на равенство всех чисел
    
    korzina = hleb1 + ' ' + hleb2 + ' ' + hleb3 + ' '
    for i in hleb:
        my_hleb[i] = korzina.count(i)
    response = f'Ваш выбор: {korzina}'
    
    return HttpResponse(response)
    
    
