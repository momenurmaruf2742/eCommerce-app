# Generated by Django 4.1 on 2024-07-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_variant_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
