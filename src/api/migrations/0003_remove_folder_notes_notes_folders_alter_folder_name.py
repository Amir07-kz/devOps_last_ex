# Generated by Django 4.0.5 on 2022-06-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_notes_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="folder",
            name="notes",
        ),
        migrations.AddField(
            model_name="notes",
            name="folders",
            field=models.ManyToManyField(to="api.folder"),
        ),
        migrations.AlterField(
            model_name="folder",
            name="name",
            field=models.CharField(max_length=50, unique=True, verbose_name="name"),
        ),
    ]
