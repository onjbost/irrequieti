# Generated by Django 4.2.5 on 2023-09-26 21:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comunication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('subject', models.TextField()),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
