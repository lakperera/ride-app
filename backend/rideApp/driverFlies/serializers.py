from rest_framework import serializers
from .models import DriverFile

class DriverFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverFile
        fields = ['file_id', 'driver', 'title', 'file_type', 'file_name', 'status','created_at','updated_at','deleted_at','file']
        extra_kwargs = {
            'driver': {'read_only': True},  # This will be set automatically
            'file_name': {'required': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'deleted_at': {'read_only': True},
        }
