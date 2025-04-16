from rest_framework import generics
from decano.models import Decano
from decano.serializers import DecanoSerializer


class DecanoCrateListView(generics.ListCreateAPIView):
    queryset = Decano.objects.all()
    serializer_class = DecanoSerializer
    

class DecanoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Decano.objects.all()
    serializer_class = DecanoSerializer