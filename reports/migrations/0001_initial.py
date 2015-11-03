# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CountryReport',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='reports.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('long', models.DecimalField(max_digits=10, verbose_name='longitude', decimal_places=6)),
                ('lat', models.DecimalField(max_digits=10, verbose_name='latitude', decimal_places=6)),
                ('default_zoom', models.IntegerField()),
                ('report', models.ForeignKey(to='reports.CountryReport')),
            ],
        ),
        migrations.CreateModel(
            name='MapPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('long', models.DecimalField(max_digits=10, decimal_places=6)),
                ('lat', models.DecimalField(max_digits=10, decimal_places=6)),
                ('map', models.ForeignKey(to='reports.Map')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('content', models.TextField(blank=True)),
                ('parent', models.ForeignKey(null=True, blank=True, related_name='children', to='reports.Section')),
                ('report', models.ForeignKey(to='reports.CountryReport')),
            ],
        ),
    ]
