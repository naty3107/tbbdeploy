# Generated by Django 3.1.4 on 2020-12-30 06:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=40),
        ),
        migrations.AlterField(
            model_name='post',
            name='background_image',
            field=models.ImageField(default='img/header.jpg', upload_to='backgrounds/2020/12/30'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 30, 6, 27, 50, 503661, tzinfo=utc)),
        ),
    ]
