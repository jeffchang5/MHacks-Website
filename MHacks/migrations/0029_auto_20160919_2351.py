# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-20 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MHacks', '0028_scanevent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scanevent',
            options={'permissions': (('can_perform_scan', 'Can perform a scan'),)},
        ),
    ]
