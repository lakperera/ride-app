from django.urls import path
from .views import create_driver,delete_driver,edit_diver,list_driver


urlpatterns = [
        path('create',create_driver.as_view() ),
        path('delete', delete_driver.as_view() ),
        path('edit', edit_diver.as_view() ),
        path('list', list_driver.as_view() ),
]