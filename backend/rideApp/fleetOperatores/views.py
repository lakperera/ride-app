from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import FleetOparetore
from .serializers import FleetOparetoreSerializer

class CreateFleetOparetore(APIView):
    def post(self, request):
        email = request.data.get('email')
        if FleetOparetore.objects.filter(email=email).exists():
            return Response(
                {"error": "A user with this email already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate status_request field
        status_request = request.data.get('status_request')
        VALID_STATUS_CHOICES = {'0', '1', '2'}
        if status_request not in VALID_STATUS_CHOICES:
            return Response(
                {"error": "Invalid status value."},
                status=status.HTTP_400_BAD_REQUEST
            )

        fleetoparetor_serializer = FleetOparetoreSerializer(data=request.data)
        if fleetoparetor_serializer.is_valid():
            fleetoparetor_serializer.save()
            return Response(fleetoparetor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(fleetoparetor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteFleetOparetore(APIView):
    def post(self, request):
        oparetore_id = request.data.get('oparetore_id')
        try:
            fleetoparetor = FleetOparetore.objects.get(oparetore_id=oparetore_id)
            if fleetoparetor.delete_oparetore:
                return Response({'error': 'Fleet operator already deleted'}, status=status.HTTP_400_BAD_REQUEST)
            
            fleetoparetor.soft_delete()  # Soft delete the fleet operator
            return Response({'message': 'Fleet operator deleted'}, status=status.HTTP_204_NO_CONTENT)
        except FleetOparetore.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)


class EditFleetOparetore(APIView):
    def put(self, request, oparetore_id):
        try:
            fleetoparetor = FleetOparetore.objects.get(oparetore_id=oparetore_id)
        except FleetOparetore.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FleetOparetoreSerializer(fleetoparetor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListFleetOparetore(APIView):
    def get(self, request):
        fleetoparetors = FleetOparetore.objects.all()
        serializer = FleetOparetoreSerializer(fleetoparetors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListPersonalFleetOparetore(APIView):
    def get(self, request):
        oparetore_id = request.query_params.get('oparetore_id')
        if oparetore_id is None:
            return Response({'error': 'Oparetore ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fleetoparetor = FleetOparetore.objects.get(oparetore_id=oparetore_id)
        except FleetOparetore.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FleetOparetoreSerializer(fleetoparetor)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RestoreFleetOparetore(APIView):
    def post(self, request):
        oparetore_id = request.data.get('oparetore_id')
        try:
            fleetoparetor = FleetOparetore.objects.get(oparetore_id=oparetore_id)
            if not fleetoparetor.delete_oparetore:
                return Response({'error': 'Fleet operator is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

            fleetoparetor.restore()  # Restore the fleet operator
            return Response({'message': 'Fleet operator restored'}, status=status.HTTP_200_OK)
        except FleetOparetore.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)
