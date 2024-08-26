from django.urls import path
from APP import views
urlpatterns = [
    path('',views.index),
    path('my_form/',views.my_form_view,name='my_form'),
    path('search/',views.search_view,name='search'),
    path('form/',views.my_post_form,name='post_form'),
    path('create/',views.create_person,name='create_person'),
    path('success/',views.success_view, name='success_url'),
]

