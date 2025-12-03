from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from .forms import CustomLoginForm  # <-- esto es clave

# Vista para el home del usuario
def user_home(request):
    return render(request, "user/user_home.html")

# Vista para login
def login_view(request):
    form = CustomLoginForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"¡Bienvenido {user.username}!")
            return redirect('blog:home')  # <-- asegúrate de que exista 'blog:home'
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, "user/login.html", {"form": form})

# Vista para registro
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # loguea al usuario automáticamente
            messages.success(request, "¡Cuenta creada con éxito!")
            return redirect('blog:home') # <-- asegúrate de tener url name="home"
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})

# Vista para logout (opcional)
def logout_view(request):
    auth_logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect('blog:home')
