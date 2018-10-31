# Generated by Django 2.0.7 on 2018-10-29 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_connection', '0001_initial'),
        ('app_services', '0007_auto_20181029_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MissingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('extension', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SQLQuery',
            fields=[
                ('Service', models.OneToOneField(limit_choices_to={'kind': 'sqlquery'}, on_delete='CASCADE', primary_key=True, related_name='query', related_query_name='query', serialize=False, to='app_services.Service')),
                ('type_name', models.CharField(max_length=50, unique=True)),
                ('query_sql', models.CharField(max_length=300)),
                ('description_fields', models.CharField(blank=True, max_length=300)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_connection.Connection')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='service',
            name='kind',
            field=models.CharField(choices=[('sqlquery', 'Consulta SQL'), ('item', 'Objetos Perdidos'), ('directory', 'Directorio de Dependencias'), ('localization', 'Geolocalizacion de Bloques')], default='sqlquery', max_length=20),
        ),
        migrations.AddField(
            model_name='service',
            name='links',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='roles',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='unique_key',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='office',
            name='Service',
            field=models.ForeignKey(limit_choices_to={'kind': 'directory'}, on_delete='CASCADE', related_name='offices', related_query_name='office', to='app_services.Service'),
        ),
        migrations.AddField(
            model_name='missingitem',
            name='Service',
            field=models.ForeignKey(limit_choices_to={'kind': 'item'}, on_delete='CASCADE', related_name='items', related_query_name='item', to='app_services.Service'),
        ),
        migrations.AddField(
            model_name='location',
            name='Service',
            field=models.ForeignKey(limit_choices_to={'kind': 'localization'}, on_delete='CASCADE', related_name='locations', related_query_name='location', to='app_services.Service'),
        ),
    ]