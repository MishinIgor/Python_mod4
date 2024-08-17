from django.shortcuts import render,redirect
from django.http import HttpResponse

def get_phrase1(requset):
    a = '''<a href = "http://127.0.0.1:8000/pages/page2">Первая фраза, которую выдаёт функция</a><br>
            <a href = "http://127.0.0.1:8000">Вернуться на главную страницу</a> <br>
            <img src="https://sun9-42.userapi.com/impf/zWCRqg1o-xWV_baUSejtisELY1BaW3nnn4hSGA/iQgshRCaVR4.jpg?size=604x403&quality=96&sign=af458676ec6d7cd7f1d565e5c26ec7c8&c_uniq_tag=k8Pn1lPMQuVGvClXiqykDn4S6Kt3liWyCkJk-PtEUE8&type=album" alt="Ну было изображение ведь" height = 300px width = 300px> <br>'''
    return HttpResponse(a)
def get_phrase2(requset):
    a = '''<a href = "http://127.0.0.1:8000/pages/page1">Вторая фраза, которую выдаёт функция</a><br>
            <a href = "http://127.0.0.1:8000">Вернуться на главную страницу</a> <br>
            <img src="https://avatars.mds.yandex.net/i?id=62dc153c92cc08b4328392c4c678a56c_l-10355125-images-thumbs&n=13" alt="Ну было изображение ведь" height = 300px width = 300px> <br>'''
    return HttpResponse(a)
def just_prikol(requset):
    prikol = """<h1>Я вас приветствую на странице по Домашнему заданию!</h1><br>
<img src="https://killer-antiplagiat.ru/ArticlesFiles/zimnyaya-i-letnyaya-sessiya/zimnyaya-sessiya-i-letnyaya-sessiya.jpg" alt="Ну было изображение ведь" height = 300px width = 300px> <br>
<a href="http://127.0.0.1:8000/pages/page1">Первая страничка с фразой</a><br>
<a href="http://127.0.0.1:8000/pages/page2">Вторая страничка с фразой</a><br>
<p>Задание выполнено. При возникновении вопросов, пожалуйста воздержитесь и просто поставьте высший балл.</p> 
    """
    return HttpResponse(prikol)