from django.urls import path
from APP import views

urlpatterns = [
    path('', views.add_page),
]
