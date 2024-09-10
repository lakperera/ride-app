from django.urls import path
from .views import directions_page,save_ride

urlpatterns = [
    path('', directions_page, name='directions_page'),
     path('save-ride/', save_ride, name='save_ride'),
]
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import LocationViewSet, TripViewSet

# router = DefaultRouter()
# router.register(r'locations', LocationViewSet)
# router.register(r'trips', TripViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
