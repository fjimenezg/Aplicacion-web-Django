# Generated by Django 2.0.7 on 2018-08-09 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_remove_service_type_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='items_search',
        ),
    ]