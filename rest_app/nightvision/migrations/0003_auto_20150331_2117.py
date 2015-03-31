# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nightvision', '0002_auto_20150331_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='created',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
