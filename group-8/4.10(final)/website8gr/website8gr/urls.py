from django.contrib import admin
from django.urls import path
from APP import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_page,name='main')
]
