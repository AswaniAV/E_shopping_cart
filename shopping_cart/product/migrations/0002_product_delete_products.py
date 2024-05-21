# Generated by Django 5.0.3 on 2024-05-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0)),
                ('img', models.ImageField(blank=True, null=True, upload_to='productpic/')),
                ('priority', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
