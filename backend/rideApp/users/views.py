from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import datetime
import jwt
from rest_framework import status


# module

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

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

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(
            key='jwt',
            value=token,
            httponly=True,
            secure=True,  # Set to True in production
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
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'successful'
        }
        return response
        
class BookingView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.Invaluser_idSignatureError:
            raise AuthenticationFailed('Invaluser_id token signature')
        except jwt.DecodeError:
            raise AuthenticationFailed('Token decode error')
        except Exception as e:
            raise AuthenticationFailed(str(e))

        user = User.objects.filter(user_id=payload['user_id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')

       
        return Response({'message': f'you can booking {user.name}'})

class CookiesPass(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.Invaluser_idSignatureError:
            raise AuthenticationFailed('Invaluser_id token signature')
        except jwt.DecodeError:
            raise AuthenticationFailed('Token decode error')
        except Exception as e:
            raise AuthenticationFailed(str(e))

        user = User.objects.filter(user_id=payload['user_id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        return Response(user.name)
