from django.urls import path
from . import views


urlpatterns = [
    path('deputados/', views.DeputadoCreateListView.as_view(), name='deputado-create-list'),
    path('deputados/<int:pk>/', views.DeputadoRetrieveUpdateDestroyView.as_view(), name='deputado-detail-view'),
]
