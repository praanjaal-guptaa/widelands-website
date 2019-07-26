# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 17:37


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlscreens', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='screenshot',
            options={'ordering': ['-category__name', 'position']},
        ),
        migrations.AddField(
            model_name='screenshot',
            name='position',
            field=models.IntegerField(blank=True, default=0, help_text=b'The position inside the category', null=True),
        ),
    ]