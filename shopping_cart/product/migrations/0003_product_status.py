# Generated by Django 5.0.3 on 2024-05-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_delete_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')], default=1),
        ),
    ]
