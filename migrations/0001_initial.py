# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bn_name', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bd_geoinfo_cityarea',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bn_name', models.CharField(max_length=50)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('website', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bd_geoinfo_district',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bn_name', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bd_geoinfo_division',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bn_name', models.CharField(max_length=50)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bd_geoinfo_union',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bn_name', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd_geoinfo.District')),
            ],
            options={
                'db_table': 'bd_geoinfo_upazila',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='union',
            name='upazila',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd_geoinfo.Upazila'),
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd_geoinfo.Division'),
        ),
        migrations.AddField(
            model_name='cityarea',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd_geoinfo.District'),
        ),
    ]
