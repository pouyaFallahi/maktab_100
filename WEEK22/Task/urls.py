from django.urls import path
from . import views
from .views import Home_page, about_me

urlpatterns = [
    path('', Home_page, name='homePage'),
    path('aboute-me/', about_me, name='git-hub')
]