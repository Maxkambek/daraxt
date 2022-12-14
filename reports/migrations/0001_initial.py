# Generated by Django 4.1.3 on 2022-11-16 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_stir', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=221)),
                ('owner_fio', models.CharField(max_length=221)),
                ('owner_jshshir', models.CharField(max_length=16)),
                ('contract_number', models.CharField(max_length=22)),
                ('description', models.TextField()),
                ('count_tree', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('number_report', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trades.district')),
                ('type_tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.typetree')),
            ],
        ),
        migrations.CreateModel(
            name='ReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='reports/')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_images', to='reports.treereport')),
            ],
        ),
    ]
