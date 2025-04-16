from rest_framework import serializers
from pacientes.models import Paciente


class PacientesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paciente
        fields = '__all__'