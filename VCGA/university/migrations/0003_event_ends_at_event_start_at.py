# Generated by Django 5.0.6 on 2024-06-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ends_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
