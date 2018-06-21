from copy import deepcopy
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from pets.models import Pet
from pets.serializers import PetSerializer

class PetView(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def update(self, request, pk=None):
        pet = self.get_object()
        serializer = self.get_serializer()

        data = deepcopy(request.data);
        
        try:
            if request.data['assignedTo']:
                data['assignedTo'] = User.objects.get(id=str(request.data['assignedTo']))
            instance = serializer.update(pet, data)
            return Response({
                'name': instance.name,
                'typePet': instance.typePet,
                'description': instance.description,
                'assignedTo': instance.assignedTo.id if instance.assignedTo else '',
            })
        except User.DoesNotExist:
            return Response({
                "error": 'User not exist'
            }, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise e
            return Response({
                "error": str(e)
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        