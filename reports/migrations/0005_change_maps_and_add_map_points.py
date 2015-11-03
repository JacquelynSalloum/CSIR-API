# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    ISSUE-40: Change maps and add map points support
    """

    dependencies = [
        ('reports', '0004_change_section_section_to_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('long', models.DecimalField(max_digits=9, decimal_places=6)),
                ('lat', models.DecimalField(max_digits=8, decimal_places=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='map',
            name='country',
        ),
        migrations.RemoveField(
            model_name='map',
            name='map_image',
        ),
        migrations.AddField(
            model_name='map',
            name='default_zoom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='lat',
            field=models.DecimalField(max_digits=8, decimal_places=6, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='long',
            field=models.DecimalField(max_digits=9, decimal_places=6, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mappoint',
            name='map',
            field=models.ForeignKey(to='reports.Map'),
        ),
    ]
