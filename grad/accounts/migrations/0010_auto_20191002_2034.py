# Generated by Django 2.2.5 on 2019-10-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20191002_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='accounts/user.png', upload_to='accounts'),
        ),
    ]
