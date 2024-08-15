from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return HttpResponse('Hello World')

def gen_numbers(request):
    #Генерация трех случай чисел от 0 до 3
    num1 = random.randint(0,3)
    num2 = random.randint(0,3)
    num3 = random.randint(0,3)
    
    #Проверка на равенство всех чисел
    if num1 == num2 == num3:
        response = f'Победа, все 3 числа равны {num1}!'
    else:
        response = f'Повезет в следующий раз! Числа: {num1}, {num2}, {num3}'
    
    return HttpResponse(response)

def hlebs(request):
    hleb = ['Булка белого','Булка чёрног','Рисовый парной']
    #Генерируем случайные хлеба
    hleb1 = random.choice(hleb)
    hleb2 = random.choice(hleb)
    hleb3 = random.choice(hleb)
    all_hleb = hleb1+' '+hleb2+' '+hleb3
    korzina = {}
    for i in hleb:
        korzina[i] = all_hleb.count(i)
    for key,value in korzina.items():
        if value==3:
            response = f'Да вы обожаете {key}'
        elif value==2:
            response = f'Хорошо когда есть такой как {key}'
        elif value==1:
            response = f'Ну да, не плохой выбор {key}'
        elif value==0:
            response = f'Да кто вообще берёт {key}'
        korzina[key] = response
    return HttpResponse(korzina)
