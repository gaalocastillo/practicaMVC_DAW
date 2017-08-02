# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('practica_mvc', '0006_auto_20170730_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('numero_recibo', models.CharField(max_length=16, serialize=False, verbose_name=b'nun recibo', primary_key=True)),
                ('fecha_pago', models.DateField(default=datetime.date.today)),
                ('nombre', models.CharField(default=b' ', max_length=200)),
                ('concepto', models.CharField(default=b' ', max_length=200)),
                ('cantidad', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
            ],
        ),
    ]
