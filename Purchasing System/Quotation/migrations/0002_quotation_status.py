# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-04 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='status',
            field=models.TextField(default='Pending', max_length=10),
        ),
    ]
