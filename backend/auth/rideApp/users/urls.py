from django.urls import path
from .views import RegisterView,LoginView,LogoutView,BookingView
from .middleware import CookiesValidation

# routes

urlpatterns = [
    path('register',RegisterView.as_view() ),
    path('login', LoginView.as_view() ),
    path('validation', CookiesValidation.as_view() ),
    path('logout', LogoutView.as_view() ),
    path('booking', BookingView.as_view() ),
]
