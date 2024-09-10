from rest_framework import serializers
from .models import BookingSetting

class BookingSettingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookingSetting  # Make sure this refers to the correct model name
        fields = [
            'booking_setting_id', 
            'booking_reference_number', 
            'symbol', 
            'Fixed_prices_priority',
            'Remove_decimal_zeros_from_price', 
            'Enable_booking_price_breakdown',
            'Auto_delete_incomplete_bookings_after', 
            'Min_booking_time', 
            'Enable_booking_cancellation', 
            'auto_refresh', 
            'refresh_time', 
            'time_counter',
            'is_enable_meeting_board', 
            'name_font_size', 
            'show_company_logo', 
            'show_in_contents', 
            'show_in_folder'
        ]

    def update(self, instance, validated_data):
        # Update the instance with validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Save the updated instance
        instance.save()  # Ensure this is called correctly
        return instance

