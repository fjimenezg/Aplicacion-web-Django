# Generated by Django 2.0.7 on 2018-08-07 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_auto_20180806_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='type_service',
        ),
    ]