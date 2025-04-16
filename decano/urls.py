from django.urls import path
from decano.view import DecanoCrateListView, DecanoRetrieveUpdateDestroyView


urlpatterns = [
    path('decano', DecanoCrateListView.as_view(), name='decano-create-list'),
    path('decano/<int:pk>', DecanoRetrieveUpdateDestroyView.as_view(), name='decano-detail-uptade'),
]