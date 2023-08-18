# Generated by Django 4.2.3 on 2023-07-27 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_description_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_modified_date',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AddField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='product',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='просмотры'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, verbose_name='описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='товар'),
        ),
    ]