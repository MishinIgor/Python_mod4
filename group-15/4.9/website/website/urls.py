from django.urls import path
from APP import views
urlpatterns = [
    path('', views.main_page,name='main'),
    path('contacts/',views.contacts,name='contacts'),
    path('aboutus/', views.aboutus,name='about_us')
]
