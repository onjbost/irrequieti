# Generated by Django 4.2 on 2023-07-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0010_remove_story_cit_remove_story_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='iframe',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
