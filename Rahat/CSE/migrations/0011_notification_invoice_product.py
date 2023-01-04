# Generated by Django 4.1.5 on 2023-01-04 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0010_online_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Message', models.TextField()),
                ('Time', models.TimeField(auto_now_add=True)),
                ('Status', models.CharField(max_length=250)),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver_ID', to='CSE.user')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender_ID', to='CSE.user')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_Product',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Qty', models.IntegerField(default=1)),
                ('Invoice_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSE.invoice')),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSE.product')),
            ],
        ),
    ]