from django.urls import path
from .views import CreateAdmin,DeleteAdmin,EditAdmin,ListAdmin,ListPersonalAdmin


urlpatterns = [
        path('createadmin',CreateAdmin.as_view()),
        path('deleteadmin', DeleteAdmin.as_view() ),
        path('editadmin', EditAdmin.as_view() ),
        path('listadmin', ListAdmin.as_view() ),
        path('personaladmin', ListPersonalAdmin.as_view() ),
]