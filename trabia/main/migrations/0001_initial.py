# Generated by Django 4.2 on 2023-05-24 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.label')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.label')),
            ],
        ),
        migrations.CreateModel(
            name='Attrazioni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.label')),
            ],
        ),
    ]
