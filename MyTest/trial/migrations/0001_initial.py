# Generated by Django 4.1.5 on 2023-01-17 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_name', models.CharField(max_length=30)),
                ('computer_type', models.CharField(max_length=30)),
                ('computer_OS', models.CharField(max_length=30)),
                ('computer_RAM', models.CharField(max_length=30)),
                ('computer_HDD', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]