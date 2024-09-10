from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DriverFile, Driver,User
from .serializers import DriverFileSerializer
import os
from admin.users.views import BookingView
import jwt
from django.conf import settings

class UploadedDriverFile(APIView):
    def post(self, request):
        # Ensure the user is authenticated
        if not request.user:
            return Response({'error': 'Unauthenticated!'}, status=status.HTTP_401_UNAUTHORIZED)

        # Extract the uploaded file
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'File is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract the file extension to determine the file type
        file_extension = os.path.splitext(file.name)[1].lower()
        valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx']
        if file_extension not in valid_extensions:
            return Response({'error': 'Unsupported file extension.'}, status=status.HTTP_400_BAD_REQUEST)

        # Assign the file type automatically
        if file_extension in ['.jpg', '.jpeg', '.png']:
            file_type = 'image'
        elif file_extension == '.pdf':
            file_type = 'pdf'
        elif file_extension in ['.doc', '.docx']:
            file_type = 'document'
        else:
            file_type = 'other'

        # Prepare the data for serialization
        data = request.data.copy()
        data['file_type'] = file_type
        file_name = os.path.splitext(file.name)[0]
        data['file_name'] = file_name

        # Ensure the driver_id is present in the request data
        driver_id = data.get('driver_id')
        if not driver_id:
            return Response({'error': 'driver_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the driver_id against the Driver model
        try:
            driver = Driver.objects.get(pk=driver_id)
        except Driver.DoesNotExist:
            return Response({'error': 'Invalid driver_id.'}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize and save the data
        serializer = DriverFileSerializer(data=request.data)
        if serializer.is_valid():
            # Set the is_createby field with the user_id who created the driver
            custom_user = getattr(request, 'user_id', None)  # Assuming user_id is available in the request
            if custom_user:
                serializer.validated_data['is_createdby'] = custom_user # Store user_id as a string
            print(custom_user)
            serializer.save(driver=driver)  # Explicitly associate with the correct Driver
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    

class ListDriverFiles(APIView):
    def get(self, request):
        driver_id = request.query_params.get('driver_id')
        if driver_id:
            files = DriverFile.objects.filter(driver_id=driver_id)
        else:
            files = DriverFile.objects.all()
        serializer = DriverFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateDriverFile(APIView):
    def put(self, request, file_id):
            try:
                file_instance = DriverFile.objects.get(file_id=file_id)
            except DriverFile.DoesNotExist:
                return Response({'error': 'DriverFile not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = DriverFileSerializer(file_instance,data=request.data, partial=True)
            if serializer.is_valid():
                custom_user = getattr(request, 'user_id', None)
                if custom_user:
                    serializer.validated_data['is_updateby'] = custom_user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteDriverFile(APIView):
    def delete(self, request, file_id):
        try:
            file_instance = DriverFile.objects.get(file_id=file_id)
        except DriverFile.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        
        file_instance.delete()
        return Response({'message': 'File deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
