# Generated by Django 4.2 on 2023-07-01 17:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('location', models.CharField(max_length=1000)),
            ],
        ),
    ]
