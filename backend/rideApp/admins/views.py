from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone

from .models import Admin
from .serializers import AdminSerializer

# Create your views here.
class CreateAdmin(APIView):
    def post(self, request):
        email = request.data.get('email')
        if Admin.objects.filter(email=email).exists():
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

        admin_serializer = AdminSerializer(data=request.data)
        if admin_serializer.is_valid():
            admin_serializer.save()  # Created_at will be handled by the model
            return Response(admin_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(admin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAdmin(APIView):
    def post(self, request):
        admin_id = request.data.get('admin_id')
        try:
            admin = Admin.objects.get(admin_id=admin_id)
            if admin.delete_admin:
                return Response({'error': 'Admin already deleted'}, status=status.HTTP_400_BAD_REQUEST)
            
            admin.soft_delete()  # Soft delete the admin
            return Response({'message': 'Admin deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Admin.DoesNotExist:
            return Response({'error': 'Admin not found'}, status=status.HTTP_404_NOT_FOUND)


class EditAdmin(APIView):
    def put(self, request, admin_id):
        try:
            driver = Driver.objects.get(admin_id=admin_id)
        except Driver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverSerializer(driver, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Updated_at will be handled by the model
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListAdmin(APIView):
    pass
    # def get(self, request):
    #     drivers = Driver.objects.all()
    #     serializer = DriverSerializer(drivers, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class ListPersonalAdmin(APIView):
    pass
    # def get(self, request):
    #     admin_id = request.query_params.get('admin_id')
    #     if admin_id is None:
    #         return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         driver = Driver.objects.get(admin_id=admin_id)
    #     except Driver.DoesNotExist:
    #         return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = DriverSerializer(driver)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class RestoreAdmin(APIView):
    pass
    # def post(self, request):
    #     admin_id = request.data.get('admin_id')
    #     try:
    #         driver = Driver.objects.get(admin_id=admin_id)
    #         if not driver.delete_users:
    #             return Response({'error': 'Driver is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

    #         driver.restore()  # Restore the driver
    #         return Response({'message': 'Driver restored'}, status=status.HTTP_200_OK)
    #     except Driver.DoesNotExist:
    #         return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
