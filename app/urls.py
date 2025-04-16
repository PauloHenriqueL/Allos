from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),  # Inclui as URLs do app 'authentication'
    path('api/v1/', include('decano.urls')),
    path('api/v1/', include('nucleo.urls')),
    path('api/v1/', include('pacientes.urls')),
    path('api/v1/', include('relatorio.urls')),
    path('api/v1/', include('Terapeuta.urls')),
]
