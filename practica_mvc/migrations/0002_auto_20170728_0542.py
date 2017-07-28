# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('practica_mvc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='id',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='nombre_empresa',
        ),
        migrations.AddField(
            model_name='factura',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0),
        ),
        migrations.AddField(
            model_name='factura',
            name='empresa',
            field=models.CharField(max_length=200, default='-'),
        ),
        migrations.AddField(
            model_name='factura',
            name='estado',
            field=models.CharField(max_length=30, default='acumulado'),
        ),
        migrations.AddField(
            model_name='factura',
            name='fecha_pago',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero_factura',
            field=models.CharField(primary_key=True, serialize=False, max_length=16, verbose_name='auth.User'),
        ),
    ]
