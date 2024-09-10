"""
URL configuration for rideApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/',include('admin.users.urls')),
    path('api/admin/jwt/driver/',include('admin.drivers.urls')),
    path('api/admin/jwt/driver-file/',include('admin.driver_files.urls')),
    path('api/admin/jwt/customer/',include('admin.customers.urls')),
    path('api/admin/jwt/passengers/',include('admin.passengers.urls')),
    path('api/admin/jwt/fleet-oparetore/',include('admin.fleet_operators.urls')),
    path('direction/',include('admin.dispatch.urls')),
    path('api/admin/jwt/vehicles/',include('admin.vehicles.urls')),
    path('api/admin/jwt/setting/',include('admin.booking_configuration.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
