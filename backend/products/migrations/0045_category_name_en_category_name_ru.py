# Generated by Django 5.0.6 on 2024-07-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0044_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
