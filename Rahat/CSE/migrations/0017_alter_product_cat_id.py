# Generated by Django 4.1.5 on 2023-01-05 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0016_alter_product_cat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Cat_ID',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='CSE.category'),
        ),
    ]