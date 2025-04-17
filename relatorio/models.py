from django.db import models
from decano.models import Decano
from Terapeuta.models import Terapeuta
from pacientes.models import Paciente


class Relatorio(models.Model):  # Cria o model
    decano = models.ForeignKey(Decano, on_delete=models.PROTECT, related_name='relatorio')
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='relatorio')
    Terapeuta = models.ForeignKey(Terapeuta, on_delete=models.PROTECT, related_name='relatorio')
    data = models.DateField(auto_now=True)
    CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Não se aplica', 'Não se aplica'),
    ]
    sessao_1_realizado = models.CharField(max_length=15, choices=CHOICES, default='Não')
    sessao_1_pago = models.CharField(max_length=15, choices=CHOICES, default='Não')
    sessao_2_realizado = models.CharField(max_length=15, choices=CHOICES, default='Não')
    sessao_2_pago = models.CharField(max_length=15, choices=CHOICES, default='Não')
    sessao_3_realizado = models.CharField(max_length=15, choices=CHOICES, default='Não')
    sessao_3_pago = models.CharField(max_length=15, choices=CHOICES, default='Não')
    sessao_4_realizado = models.CharField(max_length=15, choices=CHOICES, default='Não')
    sessao_4_pago = models.CharField(max_length=15, choices=CHOICES, default='Não')
    created_at = models.DateTimeField(auto_now_add=True)  # Insere uma data quando cria o campo
    update_at = models.DateTimeField(auto_now=True)  # Insere uma data quando edita o campo

    class Meta:  # Ordene por name
        ordering = ['Terapeuta']

    def __str__(self):  # Cite o objeto dele pelo name
        return self.Terapeuta.nome
