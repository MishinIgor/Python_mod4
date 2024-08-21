from django.urls import path
from APP import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sky/',views.sky,name='index'),
    path('city/',views.city,name='index'),
    path('image/<int:id>/',views.file_show),
    path('my_json/',views.json_show),
    path('my_file/',views.download_file),
    path('my_image/',views.download_image),
    path('picture/',views.pictures)
]
