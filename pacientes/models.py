from django.db import models
from Terapeuta.models import Terapeuta
from django.core.validators import MinValueValidator, MaxValueValidator

class Paciente(models.Model):  # Cria o model
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    contapoio = models.CharField(max_length=200, null=True, blank=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    quantidade_de_sessoes = models.FloatField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
            ]
        )# Define os valores mínimo e máximo)
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.PROTECT, related_name='pacientes')
    created_at = models.DateTimeField(auto_now_add=True)  # Insere um time quando cria o campo
    update_at = models.DateTimeField(auto_now=True)  # Insere um time quando edita o campo

    class Meta:  # Ordene por name
        ordering = ['nome']

    def __str__(self):  # Cite o objeto dele pelo name
        return self.nome
