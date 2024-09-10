from rest_framework import serializers
from .models import DriverFile
import os

class DriverFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverFile
        fields = [
            'file_id', 'driver', 'title', 'file_type', 'file_name', 
            'status', 'created_at', 'updated_at', 'deleted_at', 'file', 
            'is_aprovedby', 'is_createdby', 'is_updatedby'
        ]
        extra_kwargs = {
            'driver': {'read_only': True},  # This will be set automatically
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'deleted_at': {'read_only': True},
            'is_createdby': {'read_only': True},
            'is_updatedby': {'read_only': True},
            'is_aprovedby': {'read_only': True},
            'title': {'required': False},
            'file_name': {'required': False},
        }

    def create(self, validated_data):
        # Check file type validity
        file = validated_data.get('file',None)
        if file:
            file_extension = os.path.splitext(file.name)[1].lower()
            valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx']
            if file_extension not in valid_extensions:
                raise serializers.ValidationError({'file': 'Unsupported file extension.'})
        # Create the instance
        instance = self.Meta.model(**validated_data)

        # Save the instance
        instance.save()

        return instance