# Generated by Django 4.2.5 on 2023-09-26 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_story_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(default='helo', max_length=255),
        ),
    ]
