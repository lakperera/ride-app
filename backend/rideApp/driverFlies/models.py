from django.db import models
from drivers.models import Driver

from django.utils import timezone


class DriverFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='files')
    file_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='driver_files/')
    status = models.IntegerField(default=0) # 0-pending review 1-approved 2-rejected
    file_type = models.CharField(max_length=100, default='other') 

    created_at = models.DateTimeField(auto_now_add=True ,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.file_type})"

    def create(self):
        self.created_at =timezone.now()
        self.save()

    def update(self):
        self.updated_at =timezone.now()
        self.save()