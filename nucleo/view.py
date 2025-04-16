from rest_framework import generics
from nucleo.models import Nucleo
from nucleo.serializers import NucleoSerializer


class NucleoCrateListView(generics.ListCreateAPIView):
    queryset = Nucleo.objects.all()
    serializer_class = NucleoSerializer
    

class NucleoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nucleo.objects.all()
    serializer_class = NucleoSerializer