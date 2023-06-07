# Generated by Django 4.2 on 2023-04-11 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=50, unique=True)),
                ('bus_id', models.CharField(blank=True, max_length=50, null=True)),
                ('route', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Stopage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopage_name', models.CharField(blank=True, max_length=150, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bus')),
                ('bus_stopage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bus_stopage')),
            ],
        ),
    ]
