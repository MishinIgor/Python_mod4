from django.urls import path
from APP import views
 
urlpatterns = [
    path('my_page/', views.my_view,name='my_page'),
    path('', views.main_page,name='main_page'),
    path('contacts/', views.contacts,name='contacts'),
    path('products/', views.products,name='products'),
    path('about_us/', views.about_us,name='about_us'),
]