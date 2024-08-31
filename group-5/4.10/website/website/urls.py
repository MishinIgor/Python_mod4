from django.contrib import admin
from django.urls import path
from APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_page,name="main"),
    path('python/',views.pyth,name="python"),
    path('js/',views.js,name="js"),
    path('math/',views.math,name="math"),
]
