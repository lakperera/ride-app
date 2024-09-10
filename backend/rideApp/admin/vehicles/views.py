from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from .models import Vehicle
from .serializers import VehicleSerializer

class CreateVehicle(APIView):
    def post(self, request):
        vehicle_id = request.data.get('vehicle_id')
        if Vehicle.objects.filter(vehicle_id=vehicle_id).exists():
            return Response(
                {"error": "A vehicle with this ID already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        vehicle_serializer = VehicleSerializer(data=request.data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()  # created_at will be handled by the model
            return Response(vehicle_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(vehicle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteVehicle(APIView):
    def post(self, request, vehicle_id):
        try:
            vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
            if vehicle.status:
                return Response({'error': 'Vehicle already deleted'}, status=status.HTTP_400_BAD_REQUEST)
            
            vehicle.soft_delete()  # Soft delete the vehicle
            return Response({'message': 'Vehicle deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Vehicle.DoesNotExist:
            return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)


class EditVehicle(APIView):
    def put(self, request, vehicle_id):
        try:
            vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
        except Vehicle.DoesNotExist:
            return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # updated_at will be handled by the model
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListVehicles(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestoreVehicle(APIView):
    def post(self, request):
        vehicle_id = request.data.get('vehicle_id')
        try:
            vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
            if not vehicle.status:
                return Response({'error': 'Vehicle is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

            vehicle.restore()  # Restore the vehicle
            return Response({'message': 'Vehicle restored'}, status=status.HTTP_200_OK)
        except Vehicle.DoesNotExist:
            return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)
