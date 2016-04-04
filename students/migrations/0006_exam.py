# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20150929_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442')),
                ('date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('teacher', models.CharField(max_length=256, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
                ('group', models.OneToOneField(verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group')),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d',
                'verbose_name_plural': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d\u0438',
            },
        ),
    ]
