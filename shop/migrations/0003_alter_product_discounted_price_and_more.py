# Generated by Django 4.1 on 2024-04-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.FloatField(default=0.0),
        ),
    ]
