# Generated by Django 2.2.5 on 2019-09-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190925_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True, upload_to='accounts'),
        ),
    ]
