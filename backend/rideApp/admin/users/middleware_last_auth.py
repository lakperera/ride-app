from django.utils import timezone
from .models import User

class LastLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            User.objects.filter(user_id=request.user.user_id).update(last_login=timezone.now())
        response = self.get_response(request)
        return response
