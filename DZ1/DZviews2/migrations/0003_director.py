# Generated by Django 4.0.3 on 2022-03-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DZviews2', '0002_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mail_director', models.EmailField(max_length=254)),
                ('tel_nomber', models.CharField(max_length=100)),
            ],
        ),
    ]
