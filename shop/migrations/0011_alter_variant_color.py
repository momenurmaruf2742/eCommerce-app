# Generated by Django 4.1 on 2024-07-30 16:53

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_variant_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='color',
            field=colorfield.fields.ColorField(default='', image_field=None, max_length=25, samples=None),
        ),
    ]