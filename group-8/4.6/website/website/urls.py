from django.urls import path
from APP import views

urlpatterns = [
    path('',views.index,name='index')
]
