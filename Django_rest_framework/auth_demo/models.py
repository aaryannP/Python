from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    name = models.CharField(max_length=200)

class Order(models.Model):
    item_name = models.CharField(max_length=200)

class CartItem(models.Model):
    item_name = models.CharField(max_length=200)

class Ticket(models.Model):
    event_name = models.CharField(max_length=200)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)

