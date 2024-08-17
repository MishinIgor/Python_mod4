from django.contrib import admin
from django.urls import path
from APP.views import *

urlpatterns = [
    path('',just_prikol),
    path('pages/page1',get_phrase1,name='phrase1'),
    path('pages/page2',get_phrase2,name='phrase2'),
]