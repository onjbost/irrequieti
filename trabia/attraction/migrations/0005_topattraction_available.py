# Generated by Django 4.0.6 on 2023-07-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0004_attraction_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='topattraction',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]