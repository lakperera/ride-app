from django.urls import path
from .views import (
    CreatePassenger,
    DeletePassenger,
    EditPassenger,
    ListPassenger,
    ListPersonalPassenger,
    RestorePassenger
)

urlpatterns = [
    path('create/', CreatePassenger.as_view(), name='create_passenger'),
    path('delete/', DeletePassenger.as_view(), name='delete_passenger'),
    path('edit/<str:passenger_id>/', EditPassenger.as_view(), name='edit_passenger'),
    path('list/', ListPassenger.as_view(), name='list_passengers'),
    path('personal/', ListPersonalPassenger.as_view(), name='list_personal_passenger'),
    path('restore/', RestorePassenger.as_view(), name='restore_passenger'),
]
