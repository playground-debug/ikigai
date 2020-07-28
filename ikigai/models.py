from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    love = models.TextField(max_length=50, blank=True)
    good = models.TextField(max_length=50, blank=True)
    worldNeed = models.TextField(max_length=50, blank=True)
    paid = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}"
