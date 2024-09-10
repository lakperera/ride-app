import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ride

def directions_page(request):
    return render(request, 'directions.html')

@csrf_exempt
def save_ride(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pickup_lat = data.get('pickup_lat')
        pickup_lng = data.get('pickup_lng')
        drop_lat = data.get('drop_lat')
        drop_lng = data.get('drop_lng')
        distance = data.get('distance')
        duration = data.get('duration')
        
        board = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )

        # Save the data to the database
        # ride = Ride.objects.create(
        #     pickup_lat=pickup_lat,
        #     pickup_lng=pickup_lng,
        #     drop_lat=drop_lat,
        #     drop_lng=drop_lng,
        #     distance=distance,
        #     duration=duration
        # )
        print(pickup_lat,pickup_lng,drop_lat,drop_lng,distance,duration)
        
        return JsonResponse({'message': 'Ride saved successfully!'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# from rest_framework import viewsets
# from .models import Location, Trip
# from .serializers import LocationSerializer, TripSerializer

# class LocationViewSet(viewsets.ModelViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer

# class TripViewSet(viewsets.ModelViewSet):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer
