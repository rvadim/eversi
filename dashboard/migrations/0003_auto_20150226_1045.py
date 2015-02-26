# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselitem',
            name='cut',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='circleitem',
            name='cut',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='circleitem',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureitem',
            name='cut',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureitem',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
