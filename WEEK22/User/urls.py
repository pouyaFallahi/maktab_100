from django.urls import path
from .views import log_users, start_app, register

urlpatterns = [
    path('login-page/', log_users, name='login-page'),
    path('', start_app, name='start-app'),
    path('register-page/', register, name='register-page'),
]