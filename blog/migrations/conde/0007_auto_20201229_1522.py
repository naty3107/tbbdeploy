# Generated by Django 3.1.4 on 2020-12-29 07:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201229_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 29, 7, 22, 32, 634181, tzinfo=utc)),
        ),
    ]
