# Generated by Django 4.2.5 on 2023-10-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0019_ipmodel_story_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
