from rest_framework import serializers
from .models import Ride, ViaLocation, ReturnViaLocation, SomeoneElse

# Serializer for ViaLocation
class ViaLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViaLocation
        fields = ['via_lat', 'via_lng']

# Serializer for ReturnViaLocation
class ReturnViaLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnViaLocation
        fields = ['via_lat', 'via_lng']

# Serializer for Someone Else (if someone is booking the ride for another person)
class SomeoneElseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeoneElse
        fields = ['someone_name', 'someone_mobile_number', 'someone_email', 'ride']
        extra_kwargs = {
            'ride': {'write_only': True}  # Hide 'ride' from API response
        }
# Serializer for Ride
class RideSerializer(serializers.ModelSerializer):
    via_locations = ViaLocationSerializer(many=True, read_only=True)  # Nested serializer for via locations
    return_via_locations = ReturnViaLocationSerializer(many=True, read_only=True)  # Nested serializer for return via locations

    class Meta:
        model = Ride
        fields = [
            'pickup_lat', 'pickup_lng', 'drop_lat', 'drop_lng',
            'distance', 'duration', 'created_at',
            'return_pickup_lat', 'return_pickup_lng', 'return_drop_lat', 'return_drop_lng',
            'is_vialocation', 'is_return_vialocation', 'outbound_meet_and_greet', 'return_meet_and_greet',
            'name', 'mobile_number', 'email', 'passenger_capacity', 'suitcases_capacity',
            'carry_on_capacity', 'require_child_seat', 'drop_off_charge', 'landing_flight_number',
            'comments', 'discount_code', 'outbound_vehicle', 'return_vehicle',
            'via_locations', 'return_via_locations'  # Include nested serializers for via locations
        ]
        extra_kwargs = {
            'email': {'required': True},
            'mobile_number': {'required': True},
            'name': {'required': True},
        }


    # Optional: Additional validation
    def validate_mobile_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Mobile number must contain only digits.")
        return value
