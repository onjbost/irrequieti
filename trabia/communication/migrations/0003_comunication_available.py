# Generated by Django 4.0.6 on 2023-07-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_comunication_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunication',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
