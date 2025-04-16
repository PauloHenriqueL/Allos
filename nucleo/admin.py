from django.contrib import admin
from . import models


class NucleoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(models.Nucleo, NucleoAdmin)
