# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    ISSUE-2: Change maps to map and add title field
    """

    dependencies = [
        ('reports', '0002_change_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('map_image', models.FileField(upload_to=b'/static/maps/')),
                ('report', models.ForeignKey(to='reports.CountryReport')),
            ],
        ),
        migrations.RemoveField(
            model_name='maps',
            name='report',
        ),
        migrations.DeleteModel(
            name='Maps',
        ),
    ]
