from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_login_view(request):
    return render(request, "BaseApp/login_form.html")


def validate_login(request):
    
    user = authenticate(request, username=request.POST["Username"], password=request.POST["pass"])
    if user is not None:
        login(request, user)
        return redirect('/')

    
    return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')