# Generated by Django 5.0.6 on 2024-06-30 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_rename_categories_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]