from django.urls import path
from .views import BookingSettingView
urlpatterns = [
    path('booking-setting/<int:booking_setting_id>/', BookingSettingView.as_view(), name='booking-setting'),
    ]
