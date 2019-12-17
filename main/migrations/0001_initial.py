# Generated by Django 3.0 on 2019-12-17 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberGenerateTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(default='Pending', max_length=30)),
                ('result', models.IntegerField(default=0)),
            ],
        ),
    ]
