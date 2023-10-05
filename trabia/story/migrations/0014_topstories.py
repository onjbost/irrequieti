# Generated by Django 4.0.6 on 2023-07-05 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0013_story_fonti_story_outline'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopStories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.story')),
            ],
        ),
    ]
