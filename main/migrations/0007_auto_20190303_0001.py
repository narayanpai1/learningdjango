# Generated by Django 2.1.5 on 2019-03-02 18:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190302_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nc',
            name='comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None),
        ),
    ]
