# Generated by Django 3.0.2 on 2020-05-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodities', '0002_auto_20200525_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodityitem',
            name='price_good',
            field=models.CharField(max_length=10),
        ),
    ]
