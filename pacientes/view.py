from rest_framework import generics
from pacientes.models import Paciente
from pacientes.serializers import PacientesSerializer


class PacientesCrateListView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacientesSerializer
    

class PacientesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacientesSerializer