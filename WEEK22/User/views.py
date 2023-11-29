from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



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
    return render(request, 'register-page.html')