from django.urls import path
from APP import views

urlpatterns = [
    path('',views.index,name='index'),
    path('download_file/',views.download_file,name='download_txt'),
    path('download_image/',views.download_image,name='download_png'),
    path('picture/',views.pictures),
    path('new_page/',views.new_page)
]