from django.urls import path
from .views import UploadedDriverFile, ListDriverFiles, UpdateDriverFile, DeleteDriverFile

urlpatterns = [
    path('driver/files/', ListDriverFiles.as_view(), name='list_driver_files'),
    path('driver/file/create/', UploadedDriverFile.as_view(), name='create_driver_file'),
    path('driver/file/<int:file_id>/update/', UpdateDriverFile.as_view(), name='update_driver_file'),
    path('driver/file/<int:file_id>/delete/', DeleteDriverFile.as_view(), name='delete_driver_file'),
]
