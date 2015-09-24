# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    """
    Issue-1: Create initial model design
    """

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CountryReport',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('country', models.CharField(max_length=255)),
                ('map_url', models.CharField(max_length=255)),
                ('report', models.ForeignKey(to='reports.CountryReport')),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('report', models.ForeignKey(to='reports.CountryReport')),
                ('section', models.ForeignKey(null=True, blank=True, to='reports.Section', related_name='section_section')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('section', models.ForeignKey(related_name='table_section', to='reports.Section')),
            ],
        ),
        migrations.CreateModel(
            name='TableItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ImageTableItem',
            fields=[
                ('tableitem_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='reports.TableItem', serialize=False, auto_created=True)),
                ('image_url', models.CharField(max_length=255)),
            ],
            bases=('reports.tableitem',),
        ),
        migrations.CreateModel(
            name='TextTableItem',
            fields=[
                ('tableitem_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='reports.TableItem', serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('reports.tableitem',),
        ),
        migrations.AddField(
            model_name='tableitem',
            name='column',
            field=models.ForeignKey(to='reports.Column'),
        ),
        migrations.AddField(
            model_name='tableitem',
            name='row',
            field=models.ForeignKey(to='reports.Row'),
        ),
        migrations.AddField(
            model_name='row',
            name='table',
            field=models.ForeignKey(related_name='row_table', to='reports.Table'),
        ),
        migrations.AddField(
            model_name='content',
            name='section',
            field=models.ForeignKey(related_name='content_section', to='reports.Section'),
        ),
        migrations.AddField(
            model_name='column',
            name='table',
            field=models.ForeignKey(related_name='column_table', to='reports.Table'),
        ),
    ]
