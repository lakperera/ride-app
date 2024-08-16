from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # List other fields that are required

    def __str__(self):
        return self.email
