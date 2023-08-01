from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Category, Product
from django.views.generic import DetailView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Продукты'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'товар'
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'category', 'purchase_price', 'preview')
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.title)
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title', 'description', 'category', 'purchase_price', 'preview')

    def get_success_url(self):
        # Получаем идентификатор успешно обновленного продукта
        product_id = self.object.pk

        # Используем функцию reverse_lazy для создания URL с указанным id
        success_url = reverse_lazy('catalog:product_detail', kwargs={'pk': product_id})
        return success_url


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


def toggle_activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_published:
        product_item.is_published = False
    else:
        product_item.is_published = True

    product_item.save()

    return redirect(reverse('catalog:product_list'))
