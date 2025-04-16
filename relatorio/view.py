from rest_framework import generics
from relatorio.models import Relatorio
from relatorio.serializers import RelatorioSerializer


class RelatorioCrateListView(generics.ListCreateAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    

class RelatorioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer