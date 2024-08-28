from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DriverFile, Driver,User
from .serializers import DriverFileSerializer
import os
from users.views import BookingView
import jwt
from django.conf import settings

class UploadedDriverFile(APIView):
        def post(self, request):
            if not request.user:
                return Response({'error': 'Unauthenticated!'}, status=status.HTTP_401_UNAUTHORIZED)
                # Extract the file extension to determine the file type
            file = request.FILES.get('file')
            if not file:
                return Response({'error': 'File is required.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                
                file_extension = os.path.splitext(file.name)[1].lower()
                # Determine the file type based on the file extension
                if file_extension in ['.jpg', '.jpeg', '.png']:
                    file_type = 'image'
                elif file_extension in ['.pdf']:
                    file_type = 'pdf'
                elif file_extension in ['.doc', '.docx']:
                    file_type = 'document'
                else:
                    file_type = 'other'

                # Assign the file type automatically before saving
                data = request.data.copy()
                data['file_type'] = file_type
                # Assign the file name automatically after saving
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

                # data['is_aprovedby'] =user.name
                # data['is_createdby'] =user.name

                # Serialize and save the data
                serializer = DriverFileSerializer(data=data)
                if serializer.is_valid():
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
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return Response({'error': 'Authorization header is missing.'}, status=status.HTTP_401_UNAUTHORIZED)
            
            try:
                token = auth_header.split(' ')[1]  # "Bearer <token>"
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except IndexError:
                return Response({'error': 'Token not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
            except jwt.ExpiredSignatureError:
                return Response({'error': 'Token has expired.'}, status=status.HTTP_401_UNAUTHORIZED)
            except jwt.InvalidTokenError:
                return Response({'error': 'Invalid token.'}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
            user = User.objects.filter(user_id=payload['user_id']).first()
            try:
                file_instance = DriverFile.objects.get(file_id=file_id)
            except DriverFile.DoesNotExist:
                return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)

            data = request.data.copy()
            data['is_updatedby']=user.name
            print(user.name)
            serializer = DriverFileSerializer(file_instance,data=request.data, partial=True)
            if serializer.is_valid():
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
