from django.shortcuts import render
from rest_framework.response import Response
from .serializers import DriverSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import Driver
import datetime
from rest_framework import status


# controller
# Create your views here.

class create_driver(APIView):
    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class delete_driver(APIView):
    def post(self, request):
        unique_id = request.data.get('unique_id')
        try:
            driver = Driver.objects.get(id=unique_id)
            driver.delete()
            return Response({'message': 'Driver deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)


class edit_diver(APIView):
    def put(self, request, unique_id):
        try:
            driver = Driver.objects.get(id=unique_id)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverSerializer(driver, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class list_driver(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)