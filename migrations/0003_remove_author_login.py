# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_author_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='login',
        ),
    ]
