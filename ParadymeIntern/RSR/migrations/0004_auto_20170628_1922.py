# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-28 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0003_auto_20170628_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='graduation_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='graduation_year',
            field=models.IntegerField(default=1900),
        ),
        migrations.AlterField(
            model_name='person',
            name='major',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='school',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='school_level',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='security_clearance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='work_authorization',
            field=models.CharField(max_length=100),
        ),
    ]
