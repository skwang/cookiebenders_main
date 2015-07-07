# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_cookies', models.IntegerField(default=0, verbose_name=b'Number of cookies')),
                ('num_milk', models.IntegerField(default=0, verbose_name=b'Number of milk')),
                ('cost', models.FloatField(default=0.0, verbose_name=b'Total cost of sale')),
                ('time_start', models.DateTimeField(verbose_name=b'Request date/time')),
                ('time_deliv', models.DateTimeField(verbose_name=b'Delivery request date/time')),
                ('payment_meth', models.CharField(max_length=1, verbose_name=b'Payment method', choices=[(b'C', b'Cash'), (b'O', b'Online')])),
                ('special_req', models.TextField(max_length=5000, verbose_name=b'Special request', blank=True)),
                ('location', models.CharField(max_length=128, verbose_name=b'Delivery location')),
                ('name', models.CharField(max_length=128, verbose_name=b'Name of customer')),
                ('phone', models.CharField(max_length=16, verbose_name=b'Phone number of customer')),
                ('done_baking', models.BooleanField(default=False, verbose_name=b'Done baking')),
                ('result', models.CharField(blank=True, max_length=1, verbose_name=b'Result of sale', choices=[(b'S', b'Success'), (b'N', b'No-show'), (b'O', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceAvailable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('available', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cookie_id', models.CharField(max_length=4096, verbose_name=b'User cookie id')),
                ('default_location', models.CharField(max_length=128, verbose_name=b'Default delivery location')),
                ('default_name', models.CharField(max_length=128, verbose_name=b'Default name of customer')),
                ('default_phone', models.CharField(max_length=16, verbose_name=b'Default phone number of customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale_Baker',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('cookiebenders.sale',),
        ),
        migrations.CreateModel(
            name='Sale_Deliverer',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('cookiebenders.sale',),
        ),
    ]
