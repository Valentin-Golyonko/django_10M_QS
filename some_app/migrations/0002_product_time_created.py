# Generated by Django 3.2.9 on 2021-11-16 09:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("some_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="time_created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
