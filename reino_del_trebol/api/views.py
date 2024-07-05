from .models import Mage, Grimoire
from rest_framework import generics, status
from .serializers import MageSerializer, MagePatchSerializer, GrimoireSerializer
from rest_framework.response import Response
from .utils import GrimoireAssigner
import random

# Create your views here.
class MageView(generics.RetrieveAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer

class MageListView(generics.ListAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer

class MageCreateView(generics.CreateAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer

class MageUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer

class MageUpdateStatusView(generics.RetrieveUpdateAPIView):
    queryset = Mage.objects.all()
    serializer_class = MagePatchSerializer
    lookup_field = 'pk'

    def patch(self, request, pk, *args, **kwargs):
        try:
            instance = Mage.objects.get(pk = pk)
        except Mage.DoesNotExist:
            return Response({'error':'El id enviado no pertenece a ningun mago'}, status=status.HTTP_404_NOT_FOUND)
        
        if instance.status:
            return Response({'error':'Este mago ya fue aceptado anteriormente'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MagePatchSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid() and serializer.validated_data['status'] and not instance.status:
            
            assigner = GrimoireAssigner()
            names, weights = assigner.get_names_weights()
            random_grim = assigner.assign(names, weights)

            instance.grimoire = random_grim
            instance.save()

            serializer.save()
            msg = f'El mago fue aceptado con el grimorio: {random_grim}'
            return Response({'Accepted':msg}, status=status.HTTP_200_OK)
        
        return Response({'error':'El mago no fue aceptado'}, status=status.HTTP_404_NOT_FOUND)

class GrimoireListView(generics.ListAPIView):
    queryset = Mage.objects.all()
    serializer_class = GrimoireSerializer