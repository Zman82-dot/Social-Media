# Generated by Django 5.0 on 2023-12-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dwitter", "0002_dweet"),
    ]

    operations = [
        migrations.AddField(
            model_name="dweet",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
