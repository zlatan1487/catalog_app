from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from catalog.models import Category, Product, Version
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from config import settings
from catalog.services import get_categories_cache


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'object_list'
    success_url = reverse_lazy('catalog:index')

    extra_context = {
        'title': 'Продукты',
    }
    active_versions = Version.objects.filter(is_current_version=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_current_version=True)
        context['active_versions'] = active_versions

        # Using your function to get cached categories
        categories = get_categories_cache()
        context['category_list'] = categories

        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return Product.objects.all()
            else:
                return Product.objects.filter(
                    owner=self.request.user)
        else:
            return Product.objects.none()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = "catalog:update_product"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

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


@login_required
def categories(request):
    context = {
        'product': get_categories_cache(),
    }

    return render(request, 'product_detail.html', context)

