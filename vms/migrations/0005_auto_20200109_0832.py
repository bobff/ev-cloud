# Generated by Django 2.2.8 on 2020-01-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0004_vmdisksnap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='uuid',
            field=models.CharField(max_length=36, primary_key=True, serialize=False, verbose_name='虚拟机UUID'),
        ),
    ]
