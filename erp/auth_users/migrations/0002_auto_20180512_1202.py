# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-05-12 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]