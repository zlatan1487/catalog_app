from django.shortcuts import render
from catalog.models import Category, Product
# Create your views here.


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Все категории'
    }
    return render(request, 'catalog/categories.html', context)


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'товары из категории {category_item.title}'
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)
