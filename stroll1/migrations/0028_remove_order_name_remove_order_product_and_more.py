# Generated by Django 4.2.1 on 2023-06-21 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stroll1", "0027_shippingaddress"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="product",
        ),
        migrations.RemoveField(
            model_name="order",
            name="quantity",
        ),
    ]
