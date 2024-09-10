from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

class Passenger(AbstractUser):
    username = None
    # General input fields
   # Update fields based on new requirements
    name = models.CharField(max_length=100)
    passenger_id = models.CharField(max_length=20, unique=True,primary_key=True)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    requirment = models.CharField(max_length=100,default='pickup')
    driver_note = models.TextField(max_length=500, null=True, blank=True)
    admin_note = models.TextField(max_length=500, null=True, blank=True)
    timezone = models.CharField(max_length=63, default='UTC')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    delete_passenger = models.BooleanField(default=False)

    is_createby = models.CharField(null=False,default=False)
    is_updateby = models.CharField(null=False,default=False)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    groups = models.ManyToManyField(Group, related_name='passenger_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='passenger_permissions')

    def __str__(self):
        return self.email

    def soft_delete(self):
        self.delete_passenger = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.delete_passenger = False
        self.deleted_at = None
        self.save()
