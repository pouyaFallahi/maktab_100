from django.shortcuts import render
from .models import Tag, Task

def Home_page(request):
    items = Task.objects.all()
    tags = Tag.objects.all()
    context = {'items': items,

               }

    return render(request, 'home-page.html', context)

def about_me(request):
    return render(request, 'https://github.com/pouyaFallahi?tab=overview&from=2023-11-01&to=2023-11-28')


def search_obj(request):
    search = request.GET.get('search_box')
    finde_item = Task.objects.filter(task_title=search)
    context = {
        'sech' : finde_item,
    }

    return render(request, 'serch-page.html', context)
