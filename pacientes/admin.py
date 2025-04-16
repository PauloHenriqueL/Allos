from django.contrib import admin
from . import models


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'terapeuta', 'telefone')
    search_fields = ('nome',)


admin.site.register(models.Paciente, PacienteAdmin)
