# Generated by Django 4.2.5 on 2023-09-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Award",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("provider", models.CharField(max_length=30)),
                ("year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("provider", models.CharField(max_length=30)),
                ("year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course", models.CharField(max_length=40)),
                (
                    "course_type",
                    models.CharField(
                        choices=[("bachelor", "Bachelor"), ("other", "Other")],
                        default="other",
                        max_length=30,
                    ),
                ),
                ("institution_name", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(null=True)),
                ("until_present", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("short_description", models.CharField(max_length=40)),
                ("year", models.IntegerField()),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("url", models.URLField()),
                ("icon", models.ImageField(blank=True, null=True, upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="Work",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("company_name", models.CharField(max_length=30)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("until_present", models.BooleanField(default=False)),
            ],
        ),
    ]
