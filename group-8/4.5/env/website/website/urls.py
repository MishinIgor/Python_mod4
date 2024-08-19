from django.contrib import admin
from django.urls import path
from APP import views

urlpatterns = [
    path('', views.main_page,name='main_page'),
    path('/about_us', views.about_us,name='aboutus'),
    path('/contacts', views.contacts,name='contacts'),
]

