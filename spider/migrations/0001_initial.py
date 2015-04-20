# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockDB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('code', models.CharField(max_length=20, verbose_name=b'code')),
                ('type', models.CharField(max_length=100, verbose_name=b'type')),
                ('price', models.FloatField(default=0, verbose_name=b'latest_price')),
                ('change', models.FloatField(default=0, verbose_name=b'change_mount')),
                ('priceofYest', models.FloatField(default=0, verbose_name=b'yesterday_close_price')),
                ('priceofToda', models.FloatField(default=0, verbose_name=b'today_open_price')),
                ('priceofHigh', models.FloatField(default=0, verbose_name=b'highest_price')),
                ('priceofLow', models.FloatField(default=0, verbose_name=b'lowest_price')),
                ('inflow', models.FloatField(default=0, verbose_name=b'net_inflow')),
                ('turnoverAmount', models.FloatField(default=0, verbose_name=b'turnover_amount')),
                ('turnoverVolume', models.FloatField(default=0, verbose_name=b'turnover_volume')),
                ('turnoverRate', models.FloatField(default=0, verbose_name=b'turnover_rate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
