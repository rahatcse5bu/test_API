# Generated by Django 4.1.5 on 2023-01-05 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0015_alter_category_parent_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Cat_ID',
            field=models.ForeignKey(blank=True, default='Uncategorized', null=True, on_delete=django.db.models.deletion.CASCADE, to='CSE.category'),
        ),
    ]