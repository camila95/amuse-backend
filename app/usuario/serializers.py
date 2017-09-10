from rest_framework import serializers
from .models import *


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'


class AcudienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acudiente
        fields = '__all__'


class TelefonoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telefono
        fields = '__all__'
