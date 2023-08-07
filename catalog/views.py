from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from catalog.models import Category, Product, Version
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Продукты'}
    active_versions = Version.objects.filter(is_current_version=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_current_version=True)
        context['active_versions'] = active_versions
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'товар'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.title)
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:update_product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
        

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


