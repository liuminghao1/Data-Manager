# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150815_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area_name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scenc',
            name='scenc_name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
