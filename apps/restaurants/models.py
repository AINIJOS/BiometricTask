from django.db import models
from rest_framework.exceptions import ValidationError


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("End date cannot be before start date!")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
