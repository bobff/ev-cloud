# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compute', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='migratelog',
            options={'verbose_name': '虚拟机迁移记录', 'verbose_name_plural': '7_虚拟机迁移记录表'},
        ),
        migrations.AlterModelOptions(
            name='vmarchive',
            options={'verbose_name': '虚拟机归档记录', 'verbose_name_plural': '6_虚拟机归档表'},
        ),
        migrations.AddField(
            model_name='host',
            name='ipmi_host',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='ipmi_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='ipmi_user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='migratelog',
            name='src_undefined',
            field=models.BooleanField(default=False, verbose_name='是否清理完源主机'),
        ),
        migrations.AddField(
            model_name='vm',
            name='ha_monitored',
            field=models.BooleanField(default=False, help_text='标记是否在高可用模块监控列表中'),
        ),
    ]
