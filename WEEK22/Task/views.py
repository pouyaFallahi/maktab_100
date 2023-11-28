from django.shortcuts import render
from .models import Users, Tag, Task

def Home_page(request):
    items = Task.objects.all()
    context = {'items': items}
    return render(request, 'home-page.html', context)