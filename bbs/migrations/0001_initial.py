# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow_card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followcontent', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Send_card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('cardcontent', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tba_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=30)),
                ('ssex', models.CharField(max_length=5, choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')])),
                ('image', models.ImageField(upload_to=b'media')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='send_card',
            name='tba_user',
            field=models.ForeignKey(to='bbs.Tba_user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow_card',
            name='send_card',
            field=models.ForeignKey(to='bbs.Send_card'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow_card',
            name='tba_user',
            field=models.ForeignKey(to='bbs.Tba_user'),
            preserve_default=True,
        ),
    ]
