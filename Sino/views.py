from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

# home page view
@login_required
def Home(request):
    return render(request, 'index.html')

# register view
def RegisterView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user_data_has_error = False

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exist")
        
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exist")

        if len(password) < 6:
            user_data_has_error = True
            messages.error(request, "Password must be at least 6 characters")

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            messages.success(request, 'Acount created successfully')
            return redirect('login')

    return render(request, 'register.html')

# login view
def LoginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalide User")
            return redirect('login')

    return render(request, 'login.html')

# logout view
def LogoutView(request):
    logout(request)

    return redirect('login')