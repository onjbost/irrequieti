# Generated by Django 4.0.6 on 2023-07-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0003_topattraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
