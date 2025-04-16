from django.urls import path
from pacientes.view import PacientesCrateListView, PacientesRetrieveUpdateDestroyView


urlpatterns = [
    path('pacientes', PacientesCrateListView.as_view(), name='pacientes-create-list'),
    path('pacientes/<int:pk>', PacientesRetrieveUpdateDestroyView.as_view(), name='pacientes-detail-uptade'),
]
