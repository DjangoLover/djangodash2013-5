from django.db import models

from users.models import User
# Create your models here.


class Location(models.Model):

    user = models.OneToOneField(User)

    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)

    travel_distance = models.IntegerField(default=0, blank=True, null=True)
