from django.urls import path
from . import views
from .views import Home_page

urlpatterns = [
    path('', Home_page)
]