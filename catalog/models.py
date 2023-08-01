from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='товар')
    slug = models.CharField(max_length=200, null=True, blank=True, verbose_name="slug")
    description = models.TextField(max_length=500, verbose_name='описание товара')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    preview = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='просмотры')  # Set default value to 0
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return f'{self.title} ({self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('title',)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
