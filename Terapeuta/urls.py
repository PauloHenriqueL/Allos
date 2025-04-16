from django.urls import path
from Terapeuta.view import TerapeutaCrateListView, TerapeutaRetrieveUpdateDestroyView


urlpatterns = [
    path('terapeuta', TerapeutaCrateListView.as_view(), name='terapeuta-create-list'),
    path('terapeuta/<int:pk>', TerapeutaRetrieveUpdateDestroyView.as_view(), name='terapeuta-detail-uptade'),
]
