# Generated by Django 4.1.5 on 2023-01-04 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0007_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Cat_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSE.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSE.user'),
        ),
        migrations.AlterField(
            model_name='store',
            name='Product_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSE.product'),
        ),
    ]