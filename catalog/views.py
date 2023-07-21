from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты'
    }
    return render(request, 'catalog/index.html', context)


def product_detail_view(request, pk):

    context = {
        'title': 'товар',
        'product': get_object_or_404(Product, pk=pk)
    }
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
