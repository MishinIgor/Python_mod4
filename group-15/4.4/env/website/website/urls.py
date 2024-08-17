from django.contrib import admin
from django.urls import path,re_path
from APP import views
  
urlpatterns = [
    path("", views.index),
    path("archive", views.archive),
    path("archive/<int:year>", views.archive),
]
