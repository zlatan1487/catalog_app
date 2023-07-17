from django.urls import path
from catalog.views import index, categories, category_products, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('contacts/', contacts, name='contacts')
]