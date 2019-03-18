# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-06 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtailpages', '0051_auto_20190305_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='primarypage',
            name='banner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_banner', to='wagtailimages.Image', verbose_name='Hero Image'),
        ),
    ]