from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login', views.login, name='login'),
];


