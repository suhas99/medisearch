# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_auto_20170414_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medtypeid',
            name='medtype_id',
        ),
    ]