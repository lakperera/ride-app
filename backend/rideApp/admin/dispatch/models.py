from django.db import models

class Ride(models.Model):
    pickup_lat = models.FloatField()
    pickup_lng = models.FloatField()
    drop_lat = models.FloatField()
    drop_lng = models.FloatField()
    distance = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Return journey fields
    return_pickup_lat = models.FloatField(null=True, blank=True)
    return_pickup_lng = models.FloatField(null=True, blank=True)
    return_drop_lat = models.FloatField(null=True, blank=True)
    return_drop_lng = models.FloatField(null=True, blank=True)
    is_vialocation = models.BooleanField(default=False)
    is_return_vialocation = models.BooleanField(default=False)

    #meet and greet
    outbound_meet_and_greet = models.BooleanField(default=False)
    return_meet_and_greet = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default=False)

    passenger_capacity = models.IntegerField(null=True, blank=True)
    suitcases_capacity = models.IntegerField(null=True, blank=True)
    carry_on_capacity = models.IntegerField(null=True, blank=True)
    require_child_seat = models.BooleanField(default=False)
    drop_off_charge = models.BooleanField(default=False)
    landing_flight_number = models.CharField(max_length=50,default=True)
    comments = models.TextField(blank=True)
    discount_code = models.CharField(max_length=100,null=True, blank=True)
    vehicle =(
        ('Executive Estate', '1'),
        ('2', 'Executive Saloon (Sedan)'),
        ('3', 'Executive MPV'),
    )

    outbound_vehicle = models.CharField(max_length=100, choices=vehicle)
    return_vehicle = models.CharField(max_length=100, choices=vehicle)

    def __str__(self):
        return f"Ride from ({self.pickup_lat}, {self.pickup_lng}) to ({self.drop_lat}, {self.drop_lng})"

class ViaLocation(models.Model):
    ride = models.ForeignKey(Ride, related_name='via_locations', on_delete=models.CASCADE)
    via_lat = models.FloatField()
    via_lng = models.FloatField()

class ReturnViaLocation(models.Model):
    ride = models.ForeignKey(Ride, related_name='return_via_locations', on_delete=models.CASCADE)
    via_lat = models.FloatField()
    via_lng = models.FloatField()

    # if some one booking
class SomeoneElse(models.Model):
    ride = models.ForeignKey(Ride, related_name='someone_else', on_delete=models.CASCADE)
    someone_name = models.CharField(max_length=100)
    someone_mobile_number = models.CharField(max_length=100) 
    someone_email = models.CharField(max_length=100)
