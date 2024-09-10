from django.urls import path
from .views import ListPersonalCustomer,ListCustomer,CreateCustomer,EditCustomer,DeleteCustomer

urlpatterns = [
    path('', ListCustomer.as_view(), name='customer-list'),
    path('personal/', ListPersonalCustomer.as_view(), name='customer-detail'),
    path('create/', CreateCustomer.as_view(), name='customer-create'),
    path('update/<str:customer_id>/', EditCustomer.as_view(), name='customer-update'),
    path('delete/<str:customer_id>/',DeleteCustomer.as_view(), name='customer-delete'),
]
