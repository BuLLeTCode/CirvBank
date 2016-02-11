# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_auto_20160211_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='account_from', to='banking.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='account_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='account_to', to='banking.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Parskaitijuma datums'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Izveidosanas datums'),
        ),
    ]