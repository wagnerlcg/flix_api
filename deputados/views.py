from rest_framework import generics
from deputados.models import Deputado
from deputados.serializers import DeputadoSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class DeputadoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Deputado.objects.all()
    serializer_class = DeputadoSerializer


class DeputadoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Deputado.objects.all()
    serializer_class = DeputadoSerializer
