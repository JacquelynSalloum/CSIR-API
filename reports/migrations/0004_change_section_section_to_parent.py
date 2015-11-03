# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    ISSUE-33: Change section to parent to make it more explicit
    """

    dependencies = [
        ('reports', '0003_change_maps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='section',
        ),
        migrations.AddField(
            model_name='section',
            name='parent',
            field=models.ForeignKey(blank=True, to='reports.Section', null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='map_image',
            field=models.FileField(upload_to='/static/maps/'),
        ),
        migrations.AlterField(
            model_name='section',
            name='content',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
