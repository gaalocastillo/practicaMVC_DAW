# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practica_mvc', '0002_auto_20170728_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.CharField(choices=[('0', 'Pagado'), ('1', 'Pendiente'), ('2', 'Acumulado')], max_length=25, default='acumulado'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero_factura',
            field=models.CharField(verbose_name='Num factura', max_length=16, primary_key=True, serialize=False),
        ),
    ]
