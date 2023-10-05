# Generated by Django 4.2 on 2023-07-01 12:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_story_intro_story_intro_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('didascalia', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='cit',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='didascalia_cit',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Didascalia',
        ),
        migrations.AddField(
            model_name='citazione',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.story'),
        ),
    ]