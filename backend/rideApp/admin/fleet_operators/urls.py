from django.urls import path
from .views import (
    CreateFleetOperator,
    DeleteFleetOperator,
    EditFleetOperator,
    ListFleetOperator,
    ListPersonalFleetOperator,
    RestoreFleetOperator
)

urlpatterns = [
    path('create/', CreateFleetOperator.as_view(), name='create_fleetoparetor'),
    path('delete/', DeleteFleetOperator.as_view(), name='delete_fleetoparetor'),
    path('edit/<str:driver_id>/', EditFleetOperator.as_view(), name='edit_fleetoparetor'),
    path('list/', ListFleetOperator.as_view(), name='list_fleetoparetor'),
    path('personal/', ListPersonalFleetOperator.as_view(), name='list_personal_fleetoparetor'),
    path('restore/', RestoreFleetOperator.as_view(), name='restore_fleetoparetor'),
]
