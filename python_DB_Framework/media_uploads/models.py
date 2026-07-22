from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.name
