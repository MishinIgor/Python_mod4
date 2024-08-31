from django.contrib import admin
from django.urls import path
from APP import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_page),
    path('python/',views.pyth),
    path('js/',views.js),
    path('cpp/',views.cpp),
]
