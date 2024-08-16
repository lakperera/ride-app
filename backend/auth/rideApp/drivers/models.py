from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Driver(AbstractUser):
    # Remove first_name and last_name
    first_name = None
    last_name = None
    username = None

    # Custom fields
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # List other fields that are required

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Use a unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Use a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email
        
