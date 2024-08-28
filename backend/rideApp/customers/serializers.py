from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['email', 'password', 'customer_id', 'timezone',
                  'title', 'first_name', 'last_name', 'mobile_number',
                  'telephone_number', 'emergencey_number', 'address', 'city',
                  'postcode', 'county', 'company_name', 'company_number', 'description',
                  'company_vat_number', 'description']

        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'delete_customer': {'read_only': True},
            'deleted_at': {'read_only': True},
        }

    def create(self, validated_data):
        # Extract the password from the validated data
        password = validated_data.pop('password', None)
        
        # Create a new Customer instance with the validated data
        instance = self.Meta.model(**validated_data)

        # Set the password if provided
        if password is not None:
            instance.set_password(password)
        
        # Ensure that customer_id is set uniquely if needed
        last_customer = Customer.objects.all().order_by('-customer_id').last()
        print('last_customer', last_customer)
        
        if last_customer and last_customer.customer_id:
                # Attempt to split and extract the numeric part of the customer_id
                last_id = int(last_customer.customer_id.split('-')[1])
                new_id = last_id + 1
        else:
            new_id = 1

        # Format the new customer_id with the desired format
        formatted_customer_id = f'USR-{new_id:04d}'
        print(formatted_customer_id)
        validated_data['customer_id'] = formatted_customer_id
        # Save the instance to the database
        instance.save()
        
        return instance