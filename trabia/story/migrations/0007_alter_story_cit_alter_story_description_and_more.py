# Generated by Django 4.2 on 2023-07-01 15:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_alter_image_image_alter_story_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cit',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='didascalia_cit',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='intro',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
