from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

class Customer(AbstractUser):
    # Remove first_name and last_name
    username = None
    customer_id = models.CharField(null=False, unique=True, default=False, primary_key=True)
    password = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    timezone = models.CharField(max_length=63, default='UTC')

    # Personal inputs fields
    title = models.CharField(null=True, max_length=100)
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    mobile_number = models.IntegerField(null=True)
    telephone_number = models.IntegerField(null=True)
    emergencey_number = models.IntegerField(null=True)
    address = models.CharField(null=True, max_length=200)
    city = models.CharField(null=True, max_length=100)
    postcode = models.CharField(null=True, max_length=100)
    county = models.CharField(null=True, max_length=100)
    customer_type = models.CharField(null=True, max_length=100)

    # Company details
    company_name = models.CharField(null=True, max_length=100)
    company_number = models.CharField(null=True, max_length=100)
    description = models.TextField(null=True, max_length=500)
    company_vat_number = models.CharField(null=True, max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    delete_customer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='customer-images/', null=True)

    # Handling groups and permissions
    groups = models.ManyToManyField(Group, related_name='customer_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customer_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['customer_id']  # Ensure customer_id is a required field

    def __str__(self):
        return self.email

    def soft_delete(self):
        """Soft delete the customer by setting delete_customer to True and adding a timestamp."""
        self.delete_customer = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restore the customer by setting delete_customer to False and clearing the deleted_at timestamp."""
        self.delete_customer = False
        self.deleted_at = None
        self.save()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
