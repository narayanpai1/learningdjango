# Generated by Django 2.1.5 on 2019-03-07 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190307_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nc',
            new_name='ncnumber',
        ),
    ]
