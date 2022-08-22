from rest_framework import serializers
from .models import Compania

class CompaniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compania
        fields = ["idcompania","nombrecompania","ruc","nombrecoordinador","celular","correo"]

