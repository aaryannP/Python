from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.name
