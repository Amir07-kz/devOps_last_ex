# Generated by Django 4.0.5 on 2022-06-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="slug",
            field=models.SlugField(max_length=255, unique=True, verbose_name="slug"),
        ),
    ]
