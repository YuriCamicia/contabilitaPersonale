# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-28 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contoPersonale', '0016_auto_20180528_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conto',
            name='saldo_attuale',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=19),
        ),
        migrations.AlterField(
            model_name='conto',
            name='tot_transazioni',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=19),
        ),
    ]
