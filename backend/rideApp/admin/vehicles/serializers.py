from rest_framework import serializers
from .models import Vehicles_Types, Vehicle ,Currency

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles_Types
        fields = ['vehicle_types_id', 'vehicles_Types_name', 'active', 'display_type', 'description',
                  'vehicle_custom_image', 'passengers', 'luggage', 'hand_luggage', 'wheelchair', 
                  'booster_seats', 'child_seats', 'infant_seats', 'ordering']


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer()  # Nested serializer

    class Meta:
        model = Vehicle
        fields = [
            'vehicle_id', 'vehicle_type', 'driver', 'vehicle_image', 'registration_mark',
            'MOT', 'MOT_expiry_date', 'make', 'model', 'color', 'body_type', 'passenger_capacity',
            'registered_keeper_name', 'registered_keeper_address', 'notes', 'status', 'created_at',
            'updated_at', 'deleted_at', 'is_createby', 'is_updateby'
        ]
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'deleted_at': {'read_only': True},
            'is_createby': {'read_only': True},
            'is_updateby': {'read_only': True},
        }

    def create(self, validated_data):
        # Extract nested vehicle_type data
        vehicle_type_data = validated_data.pop('vehicle_type')

        # Check if vehicle_type already exists, if not, create it
        vehicle_type_instance, created = Vehicles_Types.objects.get_or_create(**vehicle_type_data)

        # Generate a new vehicle_id
        last_vehicle = Vehicle.objects.all().order_by('vehicle_id').last()
        if last_vehicle and last_vehicle.vehicle_id:
            last_id_number = int(last_vehicle.vehicle_id.split('-')[1])
            new_id = last_id_number + 1
        else:
            new_id = 1
        formatted_vehicle_id = f'VH-{new_id:04d}'
        validated_data['vehicle_id'] = formatted_vehicle_id

        # Create the Vehicle instance, linking it with the vehicle_type_instance
        vehicle_instance = Vehicle.objects.create(vehicle_type=vehicle_type_instance, **validated_data)

        # Set `is_createby` and `is_updateby` from the request context
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            vehicle_instance.is_createby = request.user.name
            vehicle_instance.is_updateby = request.user.name

        vehicle_instance.save()
        return vehicle_instance


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['country','currency','code','symbol']