from django.db import models
from admin.drivers.models import Driver
# from gallery.models import Gallery  # Ensure you import Gallery correctly


class Currency(models.Model):
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)


# Create your models here.
class Vehicles_Types(models.Model):
    vehicle_types_id = models.IntegerField(primary_key=True)  # Using AutoField instead of IntegerField for primary key
    vehicles_Types_name = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    display_type = models.CharField(max_length=100)  # who can view vehicle
    description = models.TextField(max_length=1000)
    
    # Gallery is linked with ForeignKey
    # gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL)
    
    vehicle_custom_image = models.FileField(upload_to='image/vehicles_custom' , null=True)  # Fixed typo 'mmodels' to 'models'
    passengers = models.IntegerField()  # Removed max_length for IntegerField
    luggage = models.IntegerField()  # Removed max_length
    hand_luggage = models.IntegerField()  # Corrected 'hand_laggage' typo
    wheelchair = models.IntegerField()  # Removed max_length
    booster_seats = models.IntegerField()  # Removed max_length
    child_seats = models.IntegerField()  # Removed max_length
    infant_seats = models.IntegerField()  # Removed max_length
    ordering = models.IntegerField()  # Removed max_length

    def __str__(self):
        return self.vehicles_Types_name


class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100)
    vehicle_name = models.CharField(max_length=100)

    # Link to Vehicle type
    vehicle_type = models.OneToOneField(Vehicles_Types, blank=True, null=True, on_delete=models.SET_NULL)  # Fixed reference to 'VehiclesTypes'

    # Assign the driver to the vehicle
    driver = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.SET_NULL)  # Allow driver to be null
    vehicle_image = models.FileField(upload_to='image/vehicles' ,null=True)  # Fixed typo 'mmodels' to 'models'
    
    registration_mark = models.CharField(max_length=100)  # Fixed typo 'registation_mark'
    MOT = models.DateField(auto_now_add=True)
    MOT_expiry_date = models.DateField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    passenger_capacity = models.IntegerField()  # Removed max_length
    registered_keeper_name = models.CharField(max_length=100)  # Fixed typo 'redistered_keeper_name'
    registered_keeper_address = models.CharField(max_length=100)  # Fixed typo 'redistered_keeper_address'
    notes = models.TextField(max_length=1000)  # Fixed 'model.TextField' to 'models.TextField'
    
    status = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Tracking who created/updated
    is_createby = models.CharField(max_length=100)
    is_updateby = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_name

    def soft_delete(self):
        self.deleted_at = timezone.now()  # Removed reference to 'delete_vehicle'
        self.save()

    def restore(self):
        self.deleted_at = None  # Restores by setting deleted_at to None
        self.save()
