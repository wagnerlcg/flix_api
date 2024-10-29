from rest_framework import generics
from eleitores.models import Eleitor
from eleitores.serializers import EleitorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class EleitorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer


class EleitorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer
