from django.urls import path
from .views import CreateDriver,DeleteDriver,EditDriver,ListDriver,ListPersonalDriver


urlpatterns = [
        path('create',CreateDriver.as_view()),
        path('delete', DeleteDriver.as_view() ),
        path('edit/<int:driver_id>/', EditDriver.as_view() ),
        path('list', ListDriver.as_view() ),
        path('personal', ListPersonalDriver.as_view() ),
]