from django.urls import path
from APP import views

urlpatterns = [
    path('profile/', views.ProfileFormView.as_view(), name='profile'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
