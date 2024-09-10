from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import FleetOperator
from .serializers import FleetOperatorSerializer

class CreateFleetOperator(APIView):
    def post(self, request):
        email = request.data.get('email')
        custom_user = getattr(request, 'user_id', None)

        if FleetOperator.objects.filter(email=email).exists():
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

        fleet_operator_serializer = FleetOperatorSerializer(data=request.data)
        if fleet_operator_serializer.is_valid():
            fleet_operator_instance = fleet_operator_serializer.save()

            if custom_user:
                # Update the fleet operator with the is_createby value
                fleet_operator_instance.is_createby = custom_user
                fleet_operator_instance.save()

            return Response(fleet_operator_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(fleet_operator_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteFleetOperator(APIView):
    def post(self, request):
        oparetore_id = request.data.get('oparetore_id')
        try:
            fleetoparetor = FleetOperator.objects.get(oparetore_id=oparetore_id)
            if fleetoparetor.delete_oparetore:
                return Response({'error': 'Fleet operator already deleted'}, status=status.HTTP_400_BAD_REQUEST)
            
            fleetoparetor.soft_delete()  # Soft delete the fleet operator
            return Response({'message': 'Fleet operator deleted'}, status=status.HTTP_204_NO_CONTENT)
        except FleetOperator.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)


class EditFleetOperator(APIView):
    def put(self, request, operator_id):
        custom_user = getattr(request, 'user_id', None)

        try:
            fleet_operator = FleetOperator.objects.get(operator_id=operator_id)
        except FleetOperator.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FleetOperatorSerializer(fleet_operator, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if custom_user:
            # Update the fleet operator with the is_updateby value
            fleet_operator.is_updateby = custom_user

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListFleetOperator(APIView):
    def get(self, request):
        fleetoparetors = FleetOperator.objects.all()
        serializer = FleetOperatorSerializer(fleetoparetors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListPersonalFleetOperator(APIView):
    def get(self, request):
        oparetore_id = request.query_params.get('oparetore_id')
        if oparetore_id is None:
            return Response({'error': 'Oparetore ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fleetoparetor = FleetOperator.objects.get(oparetore_id=oparetore_id)
        except FleetOperator.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FleetOperatorSerializer(fleetoparetor)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RestoreFleetOperator(APIView):
    def post(self, request):
        oparetore_id = request.data.get('oparetore_id')
        try:
            fleetoparetor = FleetOperator.objects.get(oparetore_id=oparetore_id)
            if not fleetoparetor.delete_oparetore:
                return Response({'error': 'Fleet operator is not deleted'}, status=status.HTTP_400_BAD_REQUEST)

            fleetoparetor.restore()  # Restore the fleet operator
            return Response({'message': 'Fleet operator restored'}, status=status.HTTP_200_OK)
        except FleetOperator.DoesNotExist:
            return Response({'error': 'Fleet operator not found'}, status=status.HTTP_404_NOT_FOUND)
