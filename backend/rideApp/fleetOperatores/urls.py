from django.urls import path
from .views import (
    CreateFleetOparetore,
    DeleteFleetOparetore,
    EditFleetOparetore,
    ListFleetOparetore,
    ListPersonalFleetOparetore,
    RestoreFleetOparetore
)

urlpatterns = [
    path('fleetoparetores/', CreateFleetOparetore.as_view(), name='create_fleetoparetor'),
    path('fleetoparetores/delete/', DeleteFleetOparetore.as_view(), name='delete_fleetoparetor'),
    path('fleetoparetores/edit/<str:driver_id>/', EditFleetOparetore.as_view(), name='edit_fleetoparetor'),
    path('fleetoparetores/list/', ListFleetOparetore.as_view(), name='list_fleetoparetor'),
    path('fleetoparetores/personal/', ListPersonalFleetOparetore.as_view(), name='list_personal_fleetoparetor'),
    path('fleetoparetores/restore/', RestoreFleetOparetore.as_view(), name='restore_fleetoparetor'),
]
