# Generated by Django 3.0.8 on 2021-08-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_auto_20210802_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='state',
            field=models.CharField(default='RAW', max_length=7),
        ),
    ]
