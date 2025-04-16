from django.urls import path
from relatorio.view import RelatorioCrateListView, RelatorioRetrieveUpdateDestroyView


urlpatterns = [
    path('relatorio', RelatorioCrateListView.as_view(), name='relatorio-create-list'),
    path('relatorio/<int:pk>', RelatorioRetrieveUpdateDestroyView.as_view(), name='relatorio-detail-uptade'),
]
