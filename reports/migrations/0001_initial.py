# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    """
    ISSUE-1: Initial model draft change
    """

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('map_url', models.CharField(max_length=255)),
                ('report', models.ForeignKey(to='reports.CountryReport')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('content', models.TextField(null=True, blank=True)),
                ('report', models.ForeignKey(to='reports.CountryReport')),
                ('section', models.ForeignKey(related_name='section_section', null=True, blank=True, to='reports.Section')),
            ],
        ),
    ]
