# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0009_medtypeid1_med_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medtypeid1',
            name='med_type',
        ),
        migrations.AlterField(
            model_name='medtypeid1',
            name='medtype_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='medtype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medtypeid1'),
        ),
    ]
