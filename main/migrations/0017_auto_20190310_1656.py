# Generated by Django 2.1.5 on 2019-03-10 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190308_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_on_comment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='nc_comments',
            name='nc',
        ),
        migrations.DeleteModel(
            name='comment_on_comment',
        ),
        migrations.DeleteModel(
            name='nc_comments',
        ),
    ]
