# Generated by Django 3.2.18 on 2023-03-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
