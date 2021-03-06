# Generated by Django 2.2.5 on 2019-09-08 14:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=50)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
