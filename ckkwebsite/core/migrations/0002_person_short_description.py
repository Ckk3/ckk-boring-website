# Generated by Django 5.0.3 on 2024-04-03 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='short_description',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
