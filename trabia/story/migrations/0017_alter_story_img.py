# Generated by Django 4.0.6 on 2023-09-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0016_topstories_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
