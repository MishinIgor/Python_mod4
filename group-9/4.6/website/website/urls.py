from django.urls import path
from APP import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dog/',views.dog,name='dog'),
    path('cat/',views.cat,name='cat'),
    path('json_show/',views.json_show,name='json_show'),
    path('picture/',views.picture,name='file_show'),
]