from rest_framework import serializers
from relatorio.models import Relatorio


class RelatorioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Relatorio
        fields = '__all__'