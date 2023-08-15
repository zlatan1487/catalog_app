from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='товар')
    description = models.TextField(max_length=500, verbose_name='описание товара')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    preview = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='фото')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('title',)


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=20, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



