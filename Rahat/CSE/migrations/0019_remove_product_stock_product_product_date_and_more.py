# Generated by Django 4.1.1 on 2023-01-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0018_alter_category_parent_id_alter_product_parent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Stock',
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_Expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_IN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_OUT',
            field=models.IntegerField(default=0),
        ),
    ]
