# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practica_mvc', '0007_recibo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='concepto',
            field=models.CharField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='nombre',
            field=models.CharField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='numero_recibo',
            field=models.CharField(primary_key=True, serialize=False, max_length=16, verbose_name='nun recibo'),
        ),
    ]
