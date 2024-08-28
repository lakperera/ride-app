from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'password', 'admin_id', 'timezone','status',
                  'title', 'first_name', 'last_name', 'mobile_number',
                  'telephone_number', 'emergencey_number', 'address', 'city',
                  'postcode', 'county', 'company_name', 'company_number', 'notes','copany_vat_number','image','delete_admin']

        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'delete_admin': {'read_only': True},
            'deleted_at': {'read_only': True},
        }

    def create(self, validated_data):
        # Handle image validation if provided
        image = validated_data.get('image', None)
        if image:
            if image.size > 2 * 1024 * 1024:  # Limit file size to 2MB
                raise serializers.ValidationError("Image size should not exceed 2MB.")

        # Pop the password and handle it separately
        password = validated_data.pop('password', None)

        # Assign an auto-incremented admin_id
        last_admin = Admin.objects.all().order_by('admin_id').first()
        if last_admin and last_admin.admin_id:
            last_id_number = int(last_admin.admin_id.split('/')[-1])
            new_id_number = last_id_number + 1
        else:
            new_id_number = 1
        formatted_admin_id = f'RA/ARV/{new_id_number:03d}'
        validated_data['admin_id'] = formatted_admin_id
        
        # Create the instance
        instance = self.Meta.model(**validated_data)

        # Set the password if provided
        if password is not None:
            instance.set_password(password)

        # Save the instance
        instance.save()

        return instance
