# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Last Name')),
                ('address', models.CharField(max_length=255, verbose_name=b'Address')),
                ('email', models.EmailField(max_length=50, verbose_name=b'Email')),
                ('phone', models.CharField(max_length=16, verbose_name=b'Phone Number')),
            ],
        ),
    ]
