# Generated by Django 3.0 on 2022-07-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_cart_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
