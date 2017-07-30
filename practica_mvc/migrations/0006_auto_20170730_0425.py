# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practica_mvc', '0005_auto_20170729_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.CharField(max_length=25, choices=[('Pagado', 'Pagado'), ('Pendiente', 'Pendiente'), ('Acumulado', 'Acumulado')], default='acumulado'),
        ),
    ]
