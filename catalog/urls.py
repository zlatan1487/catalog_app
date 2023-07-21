from django.urls import path
from catalog.views import index, contacts, product_detail_view
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_detail_view, name='product_detail_view'),  # Product detail view URL pattern
]