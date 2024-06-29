# Generated by Django 5.0.6 on 2024-06-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_productcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlist',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='faq',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='products.productcolor'),
        ),
    ]