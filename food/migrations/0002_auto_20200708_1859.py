# Generated by Django 2.2.7 on 2020-07-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='date_published',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='imageFood',
            field=models.FileField(upload_to='FoodImages'),
        ),
    ]
