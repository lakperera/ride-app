import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ride, ViaLocation, ReturnViaLocation ,SomeoneElse
from rest_framework.decorators import api_view
from .serializers import RideSerializer
from .serializers import RideSerializer, ViaLocationSerializer, ReturnViaLocationSerializer ,SomeoneElseSerializer
from django.shortcuts import render
from rest_framework import status
from django.db import transaction

def directions_page(request):
    return render(request, 'directions.html')

def directions_page_2(request):
    return render(request, 'vehicle.html')
def ditails_page(request):
    return render(request, 'details.html')

@csrf_exempt
@api_view(['POST'])
def save_ride(request):
    if request.method == 'POST':
        try:
            # Parse incoming JSON data
            data = request.data
            
            # Extract and validate ride data using the RideSerializer
            ride_serializer = RideSerializer(data=data)
            
            if ride_serializer.is_valid():
                # Save the Ride instance
                ride = ride_serializer.save()
                
                # Save via locations if provided
                via_locations = data.get('via_locations', [])
                for via in via_locations:
                    via_location_serializer = ViaLocationSerializer(data={'ride': ride_id, 'via_lat': via['via_lat'], 'via_lng': via['via_lng']})
                    if via_location_serializer.is_valid():
                        via_location_serializer.save()
                    else:
                        return JsonResponse(via_location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                # Save return via locations if provided
                return_via_locations = data.get('return_via_locations', [])
                for return_via in return_via_locations:
                    return_via_location_serializer = ReturnViaLocationSerializer(data={'ride': ride_id, 'via_lat': return_via['via_lat'], 'via_lng': return_via['via_lng']})
                    if return_via_location_serializer.is_valid():
                        return_via_location_serializer.save()
                    else:
                        return JsonResponse(return_via_location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return JsonResponse({'message': 'Ride and return journey saved successfully!'}, status=status.HTTP_201_CREATED)
            
            else:
                return JsonResponse(ride_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Catch any other error
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['PUT'])
def update_vehicles(request, ride_id):
    try:
        ride = Ride.objects.get(id=ride_id)  
    except Ride.DoesNotExist:
        return JsonResponse({'error': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = RideSerializer(ride , data=request.data , partial=True)
    serializer.is_valid(raise_exception=True)

@csrf_exempt
@api_view(['PUT'])
def update_contact_info(request, ride_id):
    print(request.data)  # Debugging input data
    try:
        # Fetch the ride object using the ride_id from the URL
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return JsonResponse({'error': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)

    # If outbound_vehicle or return_vehicle is not provided, set a default
    if request.data.get('outbound_vehicle') is None:
        request.data['outbound_vehicle'] = 'Executive Estate'  # Default value for outbound_vehicle
    if request.data.get('return_vehicle') is None:
        request.data['return_vehicle'] = 'Executive Estate'  # Default value for return_vehicle

    # Update ride details with partial update (allows for partial fields to be updated)
    serializer = RideSerializer(ride, data=request.data, partial=True)

    if serializer.is_valid():
        try:
            # Begin a transaction to ensure atomicity
            with transaction.atomic():
                # Save the updated ride details
                ride = serializer.save()

                # Process 'someone_else' data if present
                someone_else_data = request.data.get('someone_else', [])
                
                # If someone_else_data is a string, try to parse it as JSON
                if isinstance(someone_else_data, str):
                    try:
                        someone_else_data = json.loads(someone_else_data)
                    except json.JSONDecodeError:
                        return JsonResponse({'error': 'Invalid someone_else data format'}, status=status.HTTP_400_BAD_REQUEST)

                # Check if someone_else_data is a list
                if isinstance(someone_else_data, list):
                    for someone in someone_else_data:
                        # Extract and map the incoming data to the serializer field names
                        someone_name = someone.get('full_name', '')
                        someone_mobile_number = someone.get('phone_number', '')
                        someone_email = someone.get('email', '')

                        # Check if an entry already exists for this ride and person
                        someone_else_entry = SomeoneElse.objects.filter(
                            ride=ride,  # Use the ride object, not ride_id
                            someone_name=someone_name,
                            someone_mobile_number=someone_mobile_number,
                            someone_email=someone_email
                        ).first()

                        if someone_else_entry:
                            # If entry exists, update it
                            someone_else_serializer = SomeoneElseSerializer(
                                someone_else_entry, 
                                data={
                                    'ride': ride.id,  # Set ride as ride.id
                                    'someone_name': someone_name,
                                    'someone_mobile_number': someone_mobile_number,
                                    'someone_email': someone_email
                                },
                                partial=True  # Allow partial updates
                            )
                        else:
                            # If entry doesn't exist, create a new one
                            someone_else_serializer = SomeoneElseSerializer(data={
                                'ride': ride.id,  # Set ride as ride.id
                                'someone_name': someone_name,
                                'someone_mobile_number': someone_mobile_number,
                                'someone_email': someone_email
                            })

                        # Validate and save the someone_else details
                        if someone_else_serializer.is_valid():
                            someone_else_serializer.save()
                        else:
                            return JsonResponse(someone_else_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return JsonResponse({'error': 'someone_else data must be a list of objects'}, status=status.HTTP_400_BAD_REQUEST)

                # Return success response if everything goes well
                return JsonResponse({'message': 'Ride and contact info updated successfully!', 'ride_id': ride.id}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error during save: {str(e)}")  # Debugging exception handling
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        # Print the validation errors in the RideSerializer
        print("Ride Serializer Errors:", serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
