from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

def user_home(request):
    f = open ("../Heladeritrix/blog/templates/blog/user.html")
    response = HttpResponse(f.read())
    f.close()
    return response

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    f = open ("../Heladeritrix/blog/templates/blog/login.html")
    response = HttpResponse(f.read())
    f.close()

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ese usuario ya existe')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
    f = open ("../Heladeritrix/blog/templates/blog/register.html")
    response = HttpResponse(f.read())
    f.close()
