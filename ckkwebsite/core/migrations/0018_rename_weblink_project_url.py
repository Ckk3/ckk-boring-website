# Generated by Django 4.2.5 on 2023-10-05 21:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0017_project_weblink"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="weblink",
            new_name="url",
        ),
    ]
