from .models import Mage
from rest_framework import generics, status
from .serializers import MageSerializer, MagePatchSerializer
from rest_framework.response import Response

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

class MageDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Mage.objects.all()
    serializer_class = MageSerializer

class MageUpdateView(generics.RetrieveUpdateAPIView):
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
            return Response({'error':'Mage not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if instance.status:
            return Response({'error':'Status is already accepted'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MagePatchSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({'error':'Sent data is incorrect'}, status=status.HTTP_404_NOT_FOUND)
    

    # Asignar grimorios joli shit faker watefoc