# Generated by Django 4.1 on 2023-12-19 16:50

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_category_baner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_baner',
            field=models.ImageField(null=True, upload_to=category.models.category_banner_upload_to),
        ),
    ]
