# Generated by Django 4.2 on 2023-07-01 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_attrazioni_label_attrazioni_labels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='label',
        ),
        migrations.RemoveField(
            model_name='story',
            name='label',
        ),
        migrations.DeleteModel(
            name='Attrazioni',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]
