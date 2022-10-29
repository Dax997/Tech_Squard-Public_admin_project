from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login, name='login'),
    path('register_user', views.register, name='register'),
]
