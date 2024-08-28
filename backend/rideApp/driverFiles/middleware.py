from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("fuck")
        if not request.user.is_authenticated:
            return JsonResponse({"detail": "Authentication required."}, status=401)