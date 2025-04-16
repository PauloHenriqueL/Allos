from django.contrib import admin
from django.urls import path, include
from Terapeuta.view import TerapeutaCrateListView, TerapeutaRetrieveUpdateDestroyView
from relatorio.view import RelatorioCrateListView, RelatorioRetrieveUpdateDestroyView
from pacientes.view import PacientesCrateListView, PacientesRetrieveUpdateDestroyView
from nucleo.view import NucleoCrateListView, NucleoRetrieveUpdateDestroyView
from decano.view import DecanoCrateListView, DecanoRetrieveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),  # Inclui as URLs do app 'authentication'
    
    path('terapeuta', TerapeutaCrateListView.as_view(), name='terapeuta-create-list'),
    path('terapeuta/<int:pk>', TerapeutaRetrieveUpdateDestroyView.as_view(), name='terapeuta-detail-uptade'),
    
    path('relatorio', RelatorioCrateListView.as_view(), name='relatorio-create-list'),
    path('relatorio/<int:pk>', RelatorioRetrieveUpdateDestroyView.as_view(), name='relatorio-detail-uptade'),
    
    path('pacientes', PacientesCrateListView.as_view(), name='pacientes-create-list'),
    path('pacientes/<int:pk>', PacientesRetrieveUpdateDestroyView.as_view(), name='pacientes-detail-uptade'),
    
    path('nucleo', NucleoCrateListView.as_view(), name='nucleo-create-list'),
    path('nucleo/<int:pk>', NucleoRetrieveUpdateDestroyView.as_view(), name='nucleo-detail-uptade'),
    
    path('decano', DecanoCrateListView.as_view(), name='decano-create-list'),
    path('decano/<int:pk>', DecanoRetrieveUpdateDestroyView.as_view(), name='decano-detail-uptade'),
]
