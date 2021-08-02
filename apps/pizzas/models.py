from django.db import models
from apps.restaurants.models import Restaurant


class ThicknessChoices(models.TextChoices):
    S = ('S', 'Small')
    M = ('M', 'Medium')
    L = ('L', 'Large')
    XL = ('XL', 'Extra Large')


class StateChoices(models.TextChoices):
    RAW = 'RAW'
    DONE = 'DONE'


class Pizza(models.Model):
    name = models.CharField(max_length=128)
    pastry = models.CharField(
        choices=ThicknessChoices.choices,
        max_length=128,
        blank=True
    )
    cheese = models.CharField(max_length=128, blank=True)
    secret_ingredient = models.CharField(max_length=128, blank=True)
    cooking_time = models.FloatField(default=10)

    state = models.CharField(
        max_length=10,
        default='RAW'
    )

    def __str__(self):
        return self.name
