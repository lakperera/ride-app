from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone

from .models import Passenger
from .serializers import PassengerSerializer

class CreatePassenger(APIView):
    def post(self, request):
        email = request.data.get('email')
        custom_user = getattr(request, 'user_id', None)
        print(custom_user)
        
        if Passenger.objects.filter(email=email).exists():
            return Response(
                {"error": "A passenger with this email already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        passenger_serializer = PassengerSerializer(data=request.data)
        if passenger_serializer.is_valid():
            passenger_instance = passenger_serializer.save()
            
            if custom_user:
                # Update the passenger with the is_createby value
                passenger_instance.is_createby = custom_user
                passenger_instance.save()

            return Response(passenger_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePassenger(APIView):
    def post(self, request):
        passenger_id = request.data.get('passenger_id')
        try:
            passenger = Passenger.objects.get(passenger_id=passenger_id)
            if passenger.delete_users:
                return Response({'error': 'Passenger already deleted'}, status=status.HTTP_400_BAD_REQUEST)
            
            passenger.soft_delete()  # Assuming you have a soft_delete method
            return Response({'message': 'Passenger deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Passenger.DoesNotExist:
            return Response({'error': 'Passenger not found'}, status=status.HTTP_404_NOT_FOUND)

class EditPassenger(APIView):
    def put(self, request, passenger_id):
        custom_user = getattr(request, 'user_id', None)
        
        try:
            passenger = Passenger.objects.get(passenger_id=passenger_id)
        except Passenger.DoesNotExist:
            return Response({'error': 'Passenger not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PassengerSerializer(passenger, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        if custom_user:
            # Update the passenger with the is_updateby value
            passenger.is_updateby = custom_user
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListPassenger(APIView):
    def get(self, request):
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListPersonalPassenger(APIView):
    def get(self, request):
        passenger_id = request.query_params.get('passenger_id')
        if passenger_id is None:
            return Response({'error': 'Passenger ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            passenger = Passenger.objects.get(passenger_id=passenger_id)
        except Passenger.DoesNotExist:
            return Response({'error': 'Passenger not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PassengerSerializer(passenger)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RestorePassenger(APIView):
    def post(self, request):
        passenger_id = request.data.get('passenger_id')
        try:
            passenger = Passenger.objects.get(passenger_id=passenger_id)
            if not passenger.delete_users:
                return Response({'error': 'Passenger is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

            passenger.restore()  # Assuming you have a restore method
            return Response({'message': 'Passenger restored'}, status=status.HTTP_200_OK)
        except Passenger.DoesNotExist:
            return Response({'error': 'Passenger not found'}, status=status.HTTP_404_NOT_FOUND)