# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(max_length=30)),
                ('linkman', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scenc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scenc_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=30)),
                ('remake', models.CharField(max_length=90)),
                ('area', models.ForeignKey(to='data.Area')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='area',
            name='scenc',
            field=models.ForeignKey(to='data.Scenc'),
            preserve_default=True,
        ),
    ]
