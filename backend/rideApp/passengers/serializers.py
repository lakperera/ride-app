from rest_framework import serializers
from .models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['name', 'email', 'password', 'passenger_id', 'timezone',
                  'requirment', 'driver_note', 'admin_note', 'mobile_number', 'created_at', 
                  'updated_at', 'delete_passenger', 'deleted_at']

        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'delete_passenger': {'read_only': True},
            'deleted_at': {'read_only': True},
            'passenger_id': {'read_only': True},
        }

    def create(self, validated_data):

        # Pop the password and handle it separately
        password = validated_data.pop('password', None)

        # Assign an auto-incremented passenger_id
        last_passenger = Passenger.objects.all().order_by('-passenger_id').first()
        if last_passenger and last_passenger.passenger_id:
            try:
                last_id_number = int(last_passenger.passenger_id.split('-')[-1])
                new_id_number = last_id_number + 1
            except (IndexError, ValueError):
                new_id_number = 1
        else:
            new_id_number = 1

        formatted_passenger_id = f'RP-{new_id_number:03d}'
        validated_data['passenger_id'] = formatted_passenger_id

        # Create the instance
        instance = self.Meta.model(**validated_data)

        # Set the password if provided
        if password is not None:
            instance.set_password(password)

        # Save the instance
        instance.save()

        return instance
