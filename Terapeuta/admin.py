from django.contrib import admin
from . import models


class TerapeutaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nucleo', 'decano')
    search_fields = ('nome',)

admin.site.register(models.Terapeuta, TerapeutaAdmin)
