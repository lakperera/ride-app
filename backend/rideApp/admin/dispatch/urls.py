from django.urls import path
from .views import directions_page,save_ride,directions_page_2,ditails_page,update_vehicles,update_contact_info

urlpatterns = [
    path('', directions_page, name='directions_page'),
     path('save-ride/', save_ride, name='save_ride'),
     path('save-ride/vehicle/', directions_page_2, name='vehicle_page'),
     path('save-ride/vehicle/details/', ditails_page, name='vehicle_page'),
     path('update_vehicles/<int:ride_id>/', update_vehicles, name='update_vehicles'),  # Second page
    path('update_contact_info/<int:ride_id>/', update_contact_info, name='update_contact_info'),  # Third page
]
