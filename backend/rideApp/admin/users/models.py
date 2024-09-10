from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

# Create your models here.
class User(AbstractUser):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = None
    admin_category = models.CharField(max_length=100,default='local Admin')
    
    user_id = models.CharField(max_length=100, primary_key=True)
    language = models.CharField(max_length=5, choices=[], blank=True, null=True)
    is_createby = models.CharField(null=False,default=False)
    is_updateby = models.CharField(null=False,default=False)

    # get the time users are allowed to this function
    created_at = models.DateTimeField(auto_now_add=True ,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    last_login_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/admin' , null=True)

    #delete the user from the database
    delete_users=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # List other fields that are required

    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')


    def __str__(self):
        return self.email

    def soft_delete(self):
        self.delete_users = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.delete_users = False
        self.deleted_at = None
        self.save()