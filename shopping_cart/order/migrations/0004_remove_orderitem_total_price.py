# Generated by Django 5.0.6 on 2024-05-21 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='total_price',
        ),
    ]
