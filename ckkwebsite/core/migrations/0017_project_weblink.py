# Generated by Django 4.2.5 on 2023-10-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_project_is_favorite"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="weblink",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
