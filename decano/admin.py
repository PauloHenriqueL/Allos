from django.contrib import admin
from . import models


class DecanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome',)

admin.site.register(models.Decano, DecanoAdmin)
