# Generated by Django 4.0.6 on 2023-07-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0015_remove_image_story_story_available_delete_citazione_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topstories',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
