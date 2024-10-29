from django.urls import path
from . import views


urlpatterns = [
    path('vereadores/', views.VereadorCreateListView.as_view(), name='vereador-create-list'),
    path('vereadores/<int:pk>/', views.VereadorRetrieveUpdateDestroyView.as_view(), name='vereador-detail-view'),
]
