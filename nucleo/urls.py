from django.urls import path
from nucleo.view import NucleoCrateListView, NucleoRetrieveUpdateDestroyView


urlpatterns = [
    path('nucleo', NucleoCrateListView.as_view(), name='nucleo-create-list'),
    path('nucleo/<int:pk>', NucleoRetrieveUpdateDestroyView.as_view(), name='nucleo-detail-uptade'),
]