# Generated by Django 4.1.3 on 2022-11-19 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_mapreport_remove_treereport_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapreport',
            name='name',
        ),
        migrations.AddField(
            model_name='mapreport',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reports.treereport'),
        ),
    ]
