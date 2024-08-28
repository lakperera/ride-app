from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone


class Admin(AbstractUser):
    # Remove first_name and last_name
    username = None
    # general inputs  fields
    admin_id = models.CharField(null=False,unique=True , default=1 , primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    timezone = models.CharField(max_length=63, default='UTC')
    status=models.CharField(max_length=100,default='none')
    language=models.CharField(max_length=100 , default='English')


    # Personal inputs fields
    title = models.CharField(null=True,max_length=100)
    first_name = models.CharField(null=True,max_length=100)
    last_name = models.CharField(null=True,max_length=100)
    mobile_number = models.IntegerField(null=True)
    telephone_number = models.IntegerField(null=True,)
    emergencey_number = models.IntegerField(null=True,)
    address = models.CharField(null=True,max_length=200)
    city = models.CharField(null=True,max_length=100)
    postcode = models.CharField(null=True,max_length=100)
    county = models.CharField(null=True,max_length=100)
    company_name = models.CharField(null=True,max_length=100)
    company_number = models.CharField(null=True,max_length=100)
    notes = models.TextField(null=True,max_length=500)
    copany_vat_number = models.CharField(null=True,max_length=100)

   

    
    # get the time users are allowed to this function
    created_at = models.DateTimeField(auto_now_add=True ,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    #delete the user from the database
    delete_admin=models.BooleanField(default=False)

    image = models.ImageField(upload_to='admin_images/' , null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # List other fields that are required

    groups = models.ManyToManyField(
        Group,
        related_name='admin_user_set',  # Use a unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='admin_user_permissions_set',  # Use a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

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
    