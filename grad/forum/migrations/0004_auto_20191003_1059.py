# Generated by Django 2.2.5 on 2019-10-03 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20191003_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='atricle',
            new_name='article',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 3, 10, 59, 29, 140373)),
        ),
    ]
