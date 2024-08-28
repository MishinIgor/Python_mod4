from django.urls import path
from APP import views

urlpatterns = [
    path('',views.main_page,name="home"),
    path('contacts/',views.contacts,name='contacts'),
    path('about_us/',views.about_us,name='aboutus'),
]
