# Generated by Django 4.1 on 2023-12-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_baner',
            field=models.ImageField(null=True, upload_to='photo/category'),
        ),
    ]
