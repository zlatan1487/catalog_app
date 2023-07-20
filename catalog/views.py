from django.shortcuts import render
from catalog.models import Category, Product
# Create your views here.


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)
