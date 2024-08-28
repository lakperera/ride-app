from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import datetime
import jwt
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from django.conf import settings
# module

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'user_id': user.user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        response = Response()
        response.set_cookie(
            key='jwt',
            value=token,
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        response.data = {
            'jwt': token,
            'message': 'success',
        }
        return response

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class LogoutView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response

class EditUser(APIView):
    def put(self, request, user_user_id):
        try:
            user = User.objects.get(user_user_id=user_user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valuser_id(raise_exception=True)
        serializer.save()  # Updated_at will be handled by the model
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListUser(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListPersonalUser(APIView):
    def get(self, request):
        user_user_id = request.query_params.get('user_user_id')
        if user_user_id is None:
            return Response({'error': 'User user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
             user= User.objects.get(user_user_id=user_user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestoreUser(APIView):
    pass
    # def post(self, request):
    #     user_user_id = request.data.get('user_user_id')
    #     try:
    #         driver = Driver.objects.get(user_user_id=user_user_id)
    #         if not driver.delete_users:
    #             return Response({'error': 'Driver is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

    #         driver.restore()  # Restore the driver
    #         return Response({'message': 'Driver restored'}, status=status.HTTP_200_OK)
    #     except Driver.DoesNotExist:
    #         return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

class BookingView(APIView):
    def get(self, request):
        print("Getting")
        custom_user = getattr(request, 'user_name', None)
        if custom_user:
            print("Middleware custom_user:", custom_user)
            return Response({
                'name': custom_user,
                'message': 'success',
            })
        else:
            return Response({
                'detail': 'User name not found in request',
                'code': 'user_name_missing'
            }, status=400)