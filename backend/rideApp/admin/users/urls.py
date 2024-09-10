from django.urls import path
from .views import RegisterView,LoginView,LogoutView,BookingView,UserView,EditUser,ListPersonalUser

#CookiesPass

# routes

urlpatterns = [
    path('register',RegisterView.as_view() ),
    path('login', LoginView.as_view() ),
    path('jwt/logout', LogoutView.as_view() ),
    path('jwt/booking', BookingView.as_view() ),
    path('jwt/list-all', UserView.as_view() ),
    path('jwt/edit/<str:user_id>/', EditUser.as_view(), name='edit-user'),
    path('jwt/personal/', ListPersonalUser.as_view(), name='list-one-user'),
]