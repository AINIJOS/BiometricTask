# Generated by Django 3.0.8 on 2021-08-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_pizza_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='state',
            field=models.CharField(choices=[('RAW', 'Raw'), ('DONE', 'Done')], default='RAW', max_length=7),
        ),
    ]