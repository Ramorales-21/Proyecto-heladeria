from django.shortcuts import render

from django.http import HttpResponse


from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

from django.shortcuts import render

def login(request):
    return render(request, 'blog/login.html')
    return response
    
def register(request):
    return render(request, 'blog/register.html')
    return response