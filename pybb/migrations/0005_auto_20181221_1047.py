# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-21 10:47


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0004_auto_20181209_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatemessage',
            name='dst_user',
        ),
        migrations.RemoveField(
            model_name='privatemessage',
            name='src_user',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='moderators',
        ),
        migrations.DeleteModel(
            name='PrivateMessage',
        ),
    ]