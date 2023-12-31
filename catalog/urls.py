from django.urls import path
from catalog.apps import CatalogConfig
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from catalog.views import ProductListView, \
                          ProductDetailView, \
                          ContactsView, \
                          ProductCreateView, \
                          ProductUpdateView, \
                          ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(60 * 15)(ProductDetailView.as_view()), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

]
