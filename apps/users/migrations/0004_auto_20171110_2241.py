# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171110_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='users/banner/%Y/%m', verbose_name='图像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='users/image/default_big_14.png', max_length=50, upload_to='users/image/%Y/%m', verbose_name='头像'),
        ),
    ]
