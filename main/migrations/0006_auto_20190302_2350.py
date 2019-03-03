# Generated by Django 2.1.5 on 2019-03-02 18:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_dishes_filters'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='veg',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='nc',
            name='comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]
