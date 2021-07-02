from django.db import models


class ThicknessChoices(models.TextChoices):
    S = ('S', 'Small')
    M = ('M', 'Medium')
    L = ('L', 'Large')
    XL = ('XL', 'Extra Large')


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=128)
    pastry = models.CharField(
        choices=ThicknessChoices.choices,
        max_length=128,
        blank=True
    )
    cheese = models.CharField(max_length=128, blank=True)
    secret_ingredient = models.CharField(max_length=128, blank=True)

    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
        related_name='pizzas'
    )

    def __str__(self):
        return self.name

# models.SET_NULL
# models.DO_NOTHING
# models.CASCADE
