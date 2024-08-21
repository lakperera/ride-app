from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['name', 'email', 'password', 'driver_id', 'timezone',
                  'title', 'first_name', 'last_name', 'mobile_number',
                  'telephone_number', 'emergencey_number', 'address', 'city',
                  'postcode', 'county', 'company_name', 'company_number', 'notes',
                  'copany_vat_number', 'national_insurance', 'bank_account_number',
                  'insurance', 'insurance_expire_date', 'driven_license_number',
                  'driving_license_expire_date', 'poc_license_expire_date',
                  'phv_license_expire_date', 'deliver_activity_status', 'image',
                  'created_at', 'updated_at', 'delete_users', 'deleted_at','status_request']

        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'delete_users': {'read_only': True},
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

        # Assign an auto-incremented user_id
        last_driver = Driver.objects.all().order_by('-user_id').first()
        if last_driver and last_driver.user_id:
            last_id_number = int(last_driver.user_id.split('/')[-1])
            new_id_number = last_id_number + 1
        else:
            new_id_number = 1

        formatted_user_id = f'RD/DRV/{new_id_number:03d}'
        validated_data['user_id'] = formatted_user_id

        # Create the instance
        instance = self.Meta.model(**validated_data)

        # Set the password if provided
        if password is not None:
            instance.set_password(password)

        # Save the instance
        instance.save()

        return instance
