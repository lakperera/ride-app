from rest_framework import serializers
from .models import FleetOperator
from django.contrib.auth.hashers import make_password

class FleetOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetOperator
        fields = [
            'name', 'email', 'password', 'oparetore_id', 'timezone',
            'title', 'first_name', 'last_name', 'mobile_number',
            'telephone_number', 'emergencey_number', 'address', 'city',
            'postcode', 'county', 'company_name', 'company_number', 'notes',
            'copany_vat_number', 'image', 'created_at', 'updated_at',
            'delete_oparetore', 'deleted_at','language','status','date_of_birth','fleet_income','is_createby','is_updateby'
        ]

        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'delete_oparetore': {'read_only': True},
            'deleted_at': {'read_only': True},
            'is_createby': {'read_only': True},
            'is_updateby': {'read_only': True},
        }

    def create(self, validated_data):
        # Handle image validation if provided
        image = validated_data.get('image', None)
        if image:
            if image.size > 2 * 1024 * 1024:  # Limit file size to 2MB
                raise serializers.ValidationError("Image size should not exceed 2MB.")

        # Pop the password and handle it separately
        password = validated_data.pop('password', None)

        # Assign an auto-incremented oparetore_id
        last_operator = FleetOperator.objects.all().order_by('-oparetore_id').first()
        if last_operator and last_operator.oparetore_id:
            last_id_number = int(last_operator.oparetore_id.split('-')[-1])
            new_id_number = last_id_number + 1
        else:
            new_id_number = 1

        formatted_oparetore_id = f'RP-{new_id_number:03d}'
        validated_data['oparetore_id'] = formatted_oparetore_id


        if password is not None:
            validated_data['password'] = make_password(password)
        
        instance = self.Meta.model(**validated_data)
        instance.save()

        return instance
