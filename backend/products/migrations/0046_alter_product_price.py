# Generated by Django 5.0.6 on 2024-07-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_category_name_en_category_name_ru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=10000),
        ),
    ]