# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boke', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boke.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(max_length=1000, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='boke.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='标签'),
        ),
    ]