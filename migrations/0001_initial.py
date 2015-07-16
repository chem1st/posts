# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u043e\u0441\u0442\u0430')),
                ('datetime', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('content', models.TextField()),
                ('author', models.ForeignKey(to='posts.Author')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0441\u0442',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u044b',
            },
        ),
    ]
