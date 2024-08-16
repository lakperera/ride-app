from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import datetime
import jwt


# this moddle ii use to check if the user have jwt token

class CookiesValidation(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidSignatureError:
            raise AuthenticationFailed('Invalid token signature')
        except jwt.DecodeError:
            raise AuthenticationFailed('Token decode error')
        except Exception as e:
            raise AuthenticationFailed(str(e))

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        serializer = UserSerializer(user)
        return Response({
            'message': 'successful',
            'token': token,
            'data': serializer.data
        })