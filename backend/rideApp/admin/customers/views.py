from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone

from .models import Customer
from .serializers import CustomerSerializer

class CreateCustomer(APIView):
    def post(self, request):
        email = request.data.get('email')
        if Customer.objects.filter(email=email).exists():
            return Response(
                {"error": "A customer with this email already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()  # Created_at will be handled by the model
            return Response(customer_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCustomer(APIView):
    def post(self, request,customer_id):
        print(customer_id)
        try:
            customer = Customer.objects.get(customer_id=customer_id)
            if customer.delete_customer:
                return Response({'error': 'Customer already deleted'}, status=status.HTTP_400_BAD_REQUEST)
            
            customer.soft_delete()  # Soft delete the customer
            return Response({'message': 'Customer deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)


class EditCustomer(APIView):
    def put(self, request, customer_id):
        try:
            customer = Customer.objects.get(customer_id=customer_id)
            print(customer)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Updated_at will be handled by the model
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListCustomer(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListPersonalCustomer(APIView):
    def get(self, request):
        customer_id = request.query_params.get('customer_id')
        if customer_id is None:
            return Response({'error': 'Customer ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestoreCustomer(APIView):
    def post(self, request):
        customer_id = request.data.get('customer_id')
        try:
            customer = Customer.objects.get(customer_id=customer_id)
            if not customer.delete_customer:
                return Response({'error': 'Customer is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

            customer.restore()  # Restore the customer
            return Response({'message': 'Customer restored'}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
