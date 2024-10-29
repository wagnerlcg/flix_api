from django.urls import path
from . import views


urlpatterns = [
    path('eleitores/', views.EleitorCreateListView.as_view(), name='eleitor-create-list'),
    path('eleitores/<int:pk>/', views.EleitorRetrieveUpdateDestroyView.as_view(), name='eleitor-detail-view'),
]
