from django.urls import path
from . import views
from .views import Home_page, about_me, search_obj

urlpatterns = [
    path('', Home_page, name='homePage'),
    path('aboute-me/', about_me, name='git-hub'),
    path('search/', search_obj, name='search'),
]