from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BookingSetting  # Use the correct model name
from .serializers import BookingSettingSerializer
from admin.vehicles.models import Currency


class BookingSettingView(APIView):

    def put(self, request , booking_setting_id):
        
        symbol_id = request.data.get('symbol_id')

        try:
            booking = BookingSetting.objects.get(booking_setting_id=booking_setting_id)
        except booking.DoesNotExist:
            return Response({'error': 'cant access'}, status=status.HTTP_404_NOT_FOUND)


        # Deserialize and validate the incoming data
        serializer = BookingSettingSerializer(booking,data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve the symbol from the Currency model based on symbol_id
        try:
            currency_symbol = Currency.objects.get(id=symbol_id)
            symbol = currency_symbol.symbol
        except Currency.DoesNotExist:
            return Response({'error': 'Currency not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Update the symbol in the booking setting data
        serializer.validated_data['symbol'] = symbol

        # Save the updated object
        serializer.save()

        # Return the updated data
        return Response(serializer.data, status=status.HTTP_200_OK)
