from django.urls import path
from .views import CreateVehicle, DeleteVehicle, EditVehicle, ListVehicles, RestoreVehicle

urlpatterns = [
    path('create/', CreateVehicle.as_view(), name='create-vehicle'),
    path('delete/<str:vehicle_id>/', DeleteVehicle.as_view(), name='delete-vehicle'),
    path('edit/<str:vehicle_id>/', EditVehicle.as_view(), name='edit-vehicle'),
    path('list/', ListVehicles.as_view(), name='list-vehicles'),
    path('restore/', RestoreVehicle.as_view(), name='restore-vehicle'),
]
