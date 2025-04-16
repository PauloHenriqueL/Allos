from rest_framework import generics
from Terapeuta.models import Terapeuta
from Terapeuta.serializers import TerapeutaSerializer


class TerapeutaCrateListView(generics.ListCreateAPIView):
    queryset = Terapeuta.objects.all()
    serializer_class = TerapeutaSerializer
    

class TerapeutaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terapeuta.objects.all()
    serializer_class = TerapeutaSerializer