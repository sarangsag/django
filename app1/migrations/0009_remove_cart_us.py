# Generated by Django 3.0 on 2022-07-04 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_cart_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='us',
        ),
    ]
