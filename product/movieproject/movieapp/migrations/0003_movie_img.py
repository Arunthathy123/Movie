# Generated by Django 3.2.8 on 2021-12-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='exit', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
