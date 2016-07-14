# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 14:15
from __future__ import unicode_literals

from django.db import migrations

def create_eggs(apps, schema_editor):
    EggOption = apps.get_model("app.EggOption")
    EggOption.objects.create(image_url="http://66.media.tumblr.com/5e95f341b1591f576ad6a61dee4c11fb/tumblr_inline_ncu4ub1w6U1qk3xtc.gif", name="Over Easy")
    EggOption.objects.create(image_url="http://www.erench.com/RECIPES/FAVORITE/BREAK/EGGS/fegg01.gif", name="Scrambled")
    EggOption.objects.create(image_url="http://25.media.tumblr.com/ee1dc015f59d7b9c101481dcfdd292ec/tumblr_mlppn1Pxgd1s6zk05o1_r1_500.gif", name="Poached")


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_eggs)
    ]