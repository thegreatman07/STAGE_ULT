# Generated by Django 5.0.4 on 2024-05-08 13:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prix_total', models.FloatField(default=0, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.CharField(max_length=63, null=True)),
                ('done', models.BooleanField(default=False, editable=False)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DemandeLocation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('list', models.FloatField()),
                ('demande', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='location.demande')),
            ],
        ),
        migrations.DeleteModel(
            name='PropertyType',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_unit',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='unit_invoice',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='property_list',
            new_name='property_name',
        ),
        migrations.AddField(
            model_name='listing',
            name='created_by',
            field=models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='list_actuelle',
            field=models.FloatField(default=0, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='list_initiale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='proprety',
            name='list',
            field=models.FloatField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='proprety',
            name='nom',
            field=models.CharField(default=0, max_length=31),
        ),
        migrations.AddField(
            model_name='proprety',
            name='prix',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='proprety',
            name='property_number',
            field=models.CharField(default=0, max_length=31),
        ),
        migrations.AlterField(
            model_name='listing',
            name='prix',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='demandelocation',
            name='property_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.proprety'),
        ),
        migrations.DeleteModel(
            name='RentalUnity',
        ),
    ]
