# Generated by Django 4.1.5 on 2023-01-19 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=255)),
                ('manufacture', models.CharField(max_length=255)),
                ('engine_type', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('automation', models.CharField(max_length=255)),
                ('speed', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
