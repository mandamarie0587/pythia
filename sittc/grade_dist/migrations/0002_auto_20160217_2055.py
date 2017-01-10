# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_dist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eval',
            name='crsabbr',
        ),
        migrations.RemoveField(
            model_name='eval',
            name='crsno',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='course_number',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='dept_abbrev',
        ),
        migrations.AddField(
            model_name='eval',
            name='class_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='eval',
            name='course',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='grade',
            name='class_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='grade',
            name='course',
            field=models.CharField(default='', max_length=20),
        ),
    ]