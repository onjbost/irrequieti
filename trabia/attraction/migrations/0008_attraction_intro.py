# Generated by Django 4.2.5 on 2023-10-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0007_attraction_liked_likeattraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='intro',
            field=models.TextField(blank=None, default=''),
        ),
    ]
