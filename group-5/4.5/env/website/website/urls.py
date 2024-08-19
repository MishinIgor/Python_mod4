from django.urls import path
from APP import views

urlpatterns = [
    path("", views.main_page),
    path("about_us/", views.about),
    path("contacts/", views.contacts),
    path('my_page/', views.my_view,name='my_page'),
    path('products/', views.products,name='products'),
]
