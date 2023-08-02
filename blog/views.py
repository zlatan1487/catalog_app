from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview_image',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'Блог'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview_image',)

    def get_success_url(self):
        # Получаем идентификатор успешно обновленного продукта
        product_id = self.object.pk

        # Используем функцию reverse_lazy для создания URL с указанным id
        success_url = reverse_lazy('blog:view', kwargs={'pk': product_id})
        return success_url


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'О блоге'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
