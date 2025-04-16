from django.contrib import admin
from . import models


class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'Terapeuta', 'decano')
    search_fields = ('Terapeuta',)


admin.site.register(models.Relatorio, RelatorioAdmin)
