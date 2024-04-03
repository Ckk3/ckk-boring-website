# Generated by Django 5.0.3 on 2024-04-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_person_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='icon',
            field=models.CharField(choices=[('TWITTER', 'Twitter')], default='TWITTER', max_length=30),
            preserve_default=False,
        ),
    ]
