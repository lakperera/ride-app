from rest_framework import serializers
from .models import Location, Trip

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'latitude', 'longitude', 'address']

class TripSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)  # Nested serializer for Location

    class Meta:
        model = Trip
        fields = ['id', 'name', 'locations']

    def create(self, validated_data):
        locations_data = validated_data.pop('locations')
        trip = Trip.objects.create(**validated_data)

        for location_data in locations_data:
            location, created = Location.objects.get_or_create(**location_data)
            trip.locations.add(location)
        return trip
