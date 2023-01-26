# Generated by Django 4.1.5 on 2023-01-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0002_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_type', models.CharField(max_length=255)),
                ('build_owner', models.CharField(max_length=255)),
                ('build_squire', models.CharField(max_length=255)),
                ('build_rooms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_type', models.CharField(max_length=255)),
                ('build_owner', models.CharField(max_length=255)),
                ('build_squire', models.CharField(max_length=255)),
                ('build_rooms', models.IntegerField()),
            ],
        ),
    ]
