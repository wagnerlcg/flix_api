from rest_framework import generics
from vereadores.models import Vereador
from vereadores.serializers import VereadorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class VereadorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Vereador.objects.all()
    serializer_class = VereadorSerializer


class VereadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Vereador.objects.all()
    serializer_class = VereadorSerializer
