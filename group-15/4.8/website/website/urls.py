from django.urls import path
from APP import views
  
urlpatterns = [
    path("", views.index),
    path("postuser/", views.postuser),
    path('search/',views.search_view,name='search')
]