from rest_framework import serializers
from .models import Customer, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'company_number', 'description', 'company_vat_number','company_id']

class CustomerSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Customer
        fields = [
            'email', 'password', 'customer_id', 'timezone', 'title', 'first_name', 
            'last_name', 'mobile_number', 'telephone_number', 'emergencey_number', 
            'address', 'city', 'postcode', 'county', 'company', 'created_at', 'updated_at'
        ]

        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'delete_customer': {'read_only': True},
            'deleted_at': {'read_only': True},
        }

    def create(self, validated_data):
        # Extract the password and company data
        password = validated_data.pop('password', None)
        company_data = validated_data.pop('company', None)

        # Create or update the company if company_data is provided
        company_instance = None
        if company_data:
            company_instance, created = Company.objects.get_or_create(**company_data)

        # Create the customer instance
        instance = self.Meta.model(**validated_data)

        # Set the password if provided
        if password is not None:
            instance.set_password(password)

        # Assign the company to the customer
        if company_instance:
            instance.company = company_instance

        # Generate and set a unique customer_id
        last_customer = Customer.objects.all().order_by('-customer_id').last()
        if last_customer and last_customer.customer_id:
            last_id = int(last_customer.customer_id.split('-')[1])
            new_id = last_id + 1
        else:
            new_id = 1

        formatted_customer_id = f'USR-{new_id:04d}'
        instance.customer_id = formatted_customer_id

        # Save the customer instance
        instance.save()

        return instance
