# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_coach_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coach',
            name='skype',
            field=models.CharField(max_length=255),
        ),
    ]
