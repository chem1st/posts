# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.TextField(max_length=1000, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 (\u043c\u0430\u043a\u0441. 1000 \u0437\u043d\u0430\u043a\u043e\u0432)'),
        ),
    ]
