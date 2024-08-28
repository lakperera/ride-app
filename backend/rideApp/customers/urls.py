from django.urls import path
from .views import ListPersonalCustomer,ListCustomer,CreateCustomer,EditCustomer,DeleteCustomer

urlpatterns = [
    path('customers/', ListCustomer.as_view(), name='customer-list'),
    path('customers/personal/', ListPersonalCustomer.as_view(), name='customer-detail'),
    path('customers/create/', CreateCustomer.as_view(), name='customer-create'),
    path('customers/update/<str:customer_id>/', EditCustomer.as_view(), name='customer-update'),
    path('customers/delete/<str:customer_id>/',DeleteCustomer.as_view(), name='customer-delete'),
]
