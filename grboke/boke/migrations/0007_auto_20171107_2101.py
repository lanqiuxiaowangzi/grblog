# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 13:01
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boke', '0006_auto_20171107_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]