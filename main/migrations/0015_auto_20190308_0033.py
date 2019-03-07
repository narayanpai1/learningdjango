# Generated by Django 2.1.5 on 2019-03-07 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190307_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='current_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='dishes',
            name='veg',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='current_items',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dishes'),
        ),
    ]
