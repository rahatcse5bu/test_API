# Generated by Django 4.1.5 on 2023-01-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0009_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Online_Payment',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Transaction_ID', models.CharField(max_length=255)),
                ('Payment_Method', models.CharField(max_length=255)),
                ('Amount', models.FloatField()),
                ('Time', models.TimeField(auto_now_add=True)),
                ('Status', models.CharField(max_length=255)),
                ('Invoice_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSE.invoice')),
            ],
        ),
    ]
