from django.urls import path
from .views import RegisterView,LoginView,LogoutView,BookingView,UserView,CookiesPass

# routes

urlpatterns = [
    path('register',RegisterView.as_view() ),
    path('login', LoginView.as_view() ),
    path('logout', LogoutView.as_view() ),
    path('booking', BookingView.as_view() ),
    path('listall', UserView.as_view() ),
    path('cookiespass', CookiesPass.as_view() ),
]
