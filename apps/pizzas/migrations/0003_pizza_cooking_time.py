# Generated by Django 3.0.8 on 2021-07-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_remove_pizza_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='cooking_time',
            field=models.FloatField(default=10),
        ),
    ]
