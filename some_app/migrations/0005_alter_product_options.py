# Generated by Django 3.2.9 on 2021-11-16 10:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("some_app", "0004_alter_product_time_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("time_created",)},
        ),
    ]
