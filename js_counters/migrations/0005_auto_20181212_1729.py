# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-12 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_icon.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('js_counters', '0004_auto_20180209_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='countermodel',
            name='icon',
            field=djangocms_icon.fields.Icon(blank=True, default='fa-', max_length=255, verbose_name='Icon'),
        ),
        migrations.AddField(
            model_name='countermodel',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='title_image', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='counterscontainermodel',
            name='bg_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='counterscontainermodel',
            name='bg_image_position',
            field=models.CharField(blank=True, choices=[('', 'default'), ('center top', 'top'), ('center center', 'center'), ('center bottom', 'bottom'), ('left center', 'left'), ('right center', 'right'), ('left top', 'left top'), ('left bottom', 'left bottom'), ('right top', 'right top'), ('right bottom', 'right bottom')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='counterscontainermodel',
            name='bg_image_size',
            field=models.CharField(blank=True, choices=[('auto', 'default'), ('cover', 'cover'), ('contain', 'contain')], max_length=255, null=True),
        ),
    ]
