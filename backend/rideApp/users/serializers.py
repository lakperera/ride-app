from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['name','email','password','user_id','admin_category']
        extra_kwargs={
            'password':{'write_only':True},
            'admin_category':{'required':True}
        }

    def create(self, validated_data):
        # Extract the password from the validated data
        password = validated_data.pop('password', None)
        
        # Create a new User instance with the validated data
        instance = self.Meta.model(**validated_data)
        # Set the password if provided
        if password is not None:
            instance.set_password(password)
            instance.check_password(password) 
        
        # Ensure that user_id is set uniquely if needed
        if not instance.user_id:
            last_user = User.objects.all().order_by('user_id').last()
            if last_user:
                last_id = int(last_user.user_id.split('/')[1])
                new_id = last_id + 1
            else:
                new_id = 1
                instance.user_id = f'USR/{new_id:04d}'
        # Save the instance to the database
        instance.save()
        
        return instance