# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-27 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseRequisition', '0002_purchaserequisition_prid_quo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaserequisition',
            name='prid_quo',
        ),
    ]
