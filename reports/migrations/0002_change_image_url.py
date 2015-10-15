# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    """
    ISSUE-12: Add support for images
    """

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maps',
            name='map_url',
        ),
        migrations.AddField(
            model_name='maps',
            name='map_image',
            field=models.ImageField(upload_to='/static/maps/', default=None),
            preserve_default=False,
        ),
    ]
