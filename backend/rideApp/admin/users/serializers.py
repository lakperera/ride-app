from rest_framework import serializers
from .models import User
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'user_id', 'admin_category', 'created_at', 'updated_at', 'delete_users', 'deleted_at', 'is_createby', 'last_login_at','is_updateby']
        extra_kwargs = {
            'password': {'write_only': True},
            'user_id': {'read_only': True},  # Make user_id read-only
            'admin_category': {'required': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'delete_users': {'read_only': True},
            'deleted_at': {'read_only': True},
            'is_createby': {'read_only': True},
            'last_login_at': {'read_only': True},
            'is_updateby': {'read_only': True},
        }

    def create(self, validated_data):
        # Extract the password from the validated data
        password = validated_data.pop('password', None)

        # Get the last user in the database
        last_user = User.objects.all().order_by('user_id').last()
        
        # Determine the new user_id
        if last_user and last_user.user_id:
            last_id_number = int(last_user.user_id.split('-')[1])
            new_id = last_id_number + 1
        else:
            new_id = 1  # This ensures the first user gets ID 'USR-0001'

        formatted_user_id = f'USR-{new_id:04d}'
        validated_data['user_id'] = formatted_user_id

        # Create a new User instance with the validated data
        instance = self.Meta.model(**validated_data)
        
        # Set the password if provided
        if password is not None:
            instance.set_password(password)

        # Set timestamps if necessary (optional if your model doesn't handle it automatically)
        if not instance.created_at:
            instance.created_at = timezone.now()
        instance.updated_at = timezone.now()

        # Set the last login time
        instance.last_login_at = timezone.now()

        # Save the instance to the database
        instance.save()

        # Handle `is_createby` if provided in the validated data or from request context
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            instance.is_createby = request.user.name  # Adjust this according to your User model
        elif 'is_createby' in validated_data:
            instance.is_createby = validated_data['is_createby']
        
         # Handle `is_createby` if provided in the validated data or from request context
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            instance.is_updateby = request.user.name  # Adjust this according to your User model
        elif 'is_updateby' in validated_data:
            instance.is_createby = validated_data['is_updateby']

        instance.save()

        # Log the last login time for debugging (remove in production)
        print(f"last_login_at: {instance.last_login_at}")

        return instance
