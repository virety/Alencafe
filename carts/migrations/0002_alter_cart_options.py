# Generated by Django 5.0.7 on 2024-07-29 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('id',), 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
    ]