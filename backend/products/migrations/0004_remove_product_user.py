# Generated by Django 4.0.10 on 2024-06-07 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
