from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
