import jwt
from django.conf import settings
from django.http import JsonResponse
from .models import User

class TokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/booking'):
            auth_header = request.headers.get('Authorization')
            if auth_header:
                try:
                    # Decode the JWT directly from the Authorization header
                    decoded_token = jwt.decode(auth_header, settings.SECRET_KEY, algorithms=["HS256"])
                    user_id = decoded_token.get('user_id')
                    if not user_id:
                        return JsonResponse({"detail": "Token missing user_id", "code": "token_invalid"}, status=401)

                    # Retrieve the user from the database
                    try:
                        user = User.objects.get(user_id=user_id)
                        # Attach the user name to the request
                        request.user_name = user.name

                    except User.DoesNotExist:
                        return JsonResponse({"detail": "User not found", "code": "user_not_found"}, status=404)

                except jwt.ExpiredSignatureError:
                    return JsonResponse({"detail": "Token has expired", "code": "token_expired"}, status=401)
                except jwt.InvalidTokenError:
                    return JsonResponse({"detail": "Invalid token", "code": "token_invalid"}, status=401)
                except Exception as e:
                    return JsonResponse({"detail": str(e), "code": "unexpected_error"}, status=500)
            else:
                return JsonResponse({"detail": "Authorization header not provided", "code": "authorization_header_missing"}, status=401)

        response = self.get_response(request)
        return response
