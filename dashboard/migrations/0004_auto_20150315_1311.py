# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20150226_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circleitem',
            name='link',
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='link',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureitem',
            name='link',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
