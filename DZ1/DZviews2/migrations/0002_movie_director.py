# Generated by Django 4.0.3 on 2022-03-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DZviews2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Сергей Бодров', max_length=30),
        ),
    ]