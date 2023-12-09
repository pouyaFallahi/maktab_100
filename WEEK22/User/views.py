from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUser
from django.urls import reverse

def log_users(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('loging-page')
        else:
            messages.error(request, 'نام کاربری یا زمز عبور اشتباه است')

    return render (request, 'loging-page.html')


def start_app(request):
    return render(request, 'first-page.html')


def register(request):
    if request.method == "POST":
        form_register = RegisterUser(request.POST)
        if form_register.is_valid():
            obj = form_register.save()
            return redirect(reverse('homePage'))


    elif request.method == "GET":
        form_register = RegisterUser()
        context = {
            'form_register': form_register,
        }

    return render(request, 'register-page.html', context)