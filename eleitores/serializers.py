from rest_framework import serializers
from eleitores.models import Eleitor


class EleitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eleitor
        fields = '__all__'
