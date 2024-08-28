from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone

from .models import Driver
from .serializers import DriverSerializer

class CreateDriver(APIView):
    def post(self, request):
        email = request.data.get('email')
        if Driver.objects.filter(email=email).exists():
            return Response(
                {"error": "A user with this email already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        status_id = request.data.get('deliver_activity_status')
        VALID_STATUS_CHOICES = {'1', '2', '3'}
        if status_id not in VALID_STATUS_CHOICES:
            return Response(
                {"error": "Invalid status value."},
                status=status.HTTP_400_BAD_REQUEST
            )

        status_request = request.data.get('status_request')
        VALID_STATUS_CHOICES = {'0', '1', '2'}
        if status_request not in VALID_STATUS_CHOICES:
            return Response(
                {"error": "Invalid status value."},
                status=status.HTTP_400_BAD_REQUEST
            )

        driver_serializer = DriverSerializer(data=request.data)
        if driver_serializer.is_valid():
            driver_serializer.save()  # Created_at will be handled by the model
            return Response(driver_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(driver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteDriver(APIView):
    def post(self, request):
        driver_id = request.data.get('driver_id')
        try:
            driver = Driver.objects.get(driver_id=driver_id)
            if driver.delete_users:
                return Response({'error': 'Driver already deleted'}, status=status.HTTP_400_BAD_REQUEST)
            
            driver.soft_delete()  # Soft delete the driver
            return Response({'message': 'Driver deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)


class EditDriver(APIView):
    def put(self, request, driver_id):
        print(driver_id)
        try:
            driver = Driver.objects.get(driver_id=driver_id)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverSerializer(driver, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Updated_at will be handled by the model
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListDriver(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListPersonalDriver(APIView):
    def get(self, request):
        driver_id = request.query_params.get('driver_id')
        print(driver_id)
        if driver_id is None:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            driver = Driver.objects.get(driver_id=driver_id)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverSerializer(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestoreDriver(APIView):
    def post(self, request):
        driver_id = request.data.get('driver_id')
        try:
            driver = Driver.objects.get(driver_id=driver_id)
            if not driver.delete_users:
                return Response({'error': 'Driver is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

            driver.restore()  # Restore the driver
            return Response({'message': 'Driver restored'}, status=status.HTTP_200_OK)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
