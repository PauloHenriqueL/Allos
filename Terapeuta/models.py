from django.db import models
from decano.models import Decano
from nucleo.models import Nucleo


class Terapeuta(models.Model):  # Cria o model
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    decano = models.ForeignKey(Decano, on_delete=models.PROTECT, related_name='terapeuta', null=True, blank=True)
    nucleo  = models.ForeignKey(Nucleo, on_delete=models.PROTECT, related_name='terapeuta', null=True, blank=True)
    abordagem = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Insere um time quando cria o campo
    update_at = models.DateTimeField(auto_now=True)  # Insere um time quando edita o campo


    class Meta:  # Ordene por name
        ordering = ['nome']


    def __str__(self):  # Cite o objeto dele pelo name
        return self.nome
