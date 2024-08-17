from django.shortcuts import render,redirect
from django.http import HttpResponse

def get_phrase1(requset):
    a = '''<a href = "http://127.0.0.1:8000/pages/page2">Первая фраза, которую выдаёт функция</a>
            <a href = "http://127.0.0.1:8000">Вернуться на главную страницу</a>'''
    return HttpResponse(a)
def get_phrase2(requset):
    a = '''<a href = "http://127.0.0.1:8000/pages/page1">Вторая фраза, которую выдаёт функция</a>
            <a href = "http://127.0.0.1:8000">Вернуться на главную страницу</a>'''
    return HttpResponse(a)
def just_prikol(requset):
    prikol = """<h1>Я вас приветствую на странице по Домашнему заданию!</h1>
<img src="https://killer-antiplagiat.ru/ArticlesFiles/zimnyaya-i-letnyaya-sessiya/zimnyaya-sessiya-i-letnyaya-sessiya.jpg" alt="Ну было изображение ведь">
<a href="http://127.0.0.1:8000/pages/page1">Первая страничка с фразой</a>
<a href="http://127.0.0.1:8000/pages/page2">Вторая страничка с фразой</a>
<p>Задание выполнено. При возникновении вопросов, пожалуйста воздержитесь и просто поставьте высший балл.</p> 
    """
    return HttpResponse(prikol)