from django.db import models
from django.contrib.postgres.fields import ArrayField

class Ride(models.Model):
    pickup_lat = models.FloatField()
    pickup_lng = models.FloatField()
    drop_lat = models.FloatField()
    drop_lng = models.FloatField()
    distance = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # define the array for store the via location
    via_lat = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )
    via_lang = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )

    def __str__(self):
        return f"Ride from ({self.pickup_lat}, {self.pickup_lng}) to ({self.drop_lat}, {self.drop_lng})"

class Via_Location(models.Model):
    name = models.CharField(max_length=255)
    locations = models.ManyToManyField(Location, related_name='trips')