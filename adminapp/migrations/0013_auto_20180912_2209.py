# Generated by Django 2.0.7 on 2018-09-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_auto_20180908_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='relationship',
        ),
        migrations.AddField(
            model_name='service',
            name='relationships',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
