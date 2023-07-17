from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='товар')
    description = models.TextField(verbose_name='описание товара')
    image = models.ImageField(upload_to='product_images', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    creation_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('title',)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(**NULLABLE, verbose_name='описание')
#     created_at = models.BooleanField(default=True, verbose_name='created')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
