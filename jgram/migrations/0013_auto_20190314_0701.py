# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-14 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jgram', '0012_auto_20190313_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
