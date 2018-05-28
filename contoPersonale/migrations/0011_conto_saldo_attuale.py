# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contoPersonale', '0010_remove_transazione_saldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='conto',
            name='saldo_attuale',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
    ]