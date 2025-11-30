from django.shortcuts import render

from django.http import HttpResponse


from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def login(request):
    f = open ("../Heladeritrix/blog/templates/blog/login.html")
    response = HttpResponse(f.read())
    f.close()
    return response

def register(request):
    f = open ("../Heladeritrix/blog/templates/blog/register.html")
    response = HttpResponse(f.read())
    f.close()
    return response