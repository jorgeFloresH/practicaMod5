from rest_framework import serializers
from .models import Predio
from .models import direccion
from .models import foto

class PredioSerializer(serializers.ModelSerializer):
    class Meta:
        model =Predio
        fields= "__all__"

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model =direccion
        fields= "__all__"

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model =foto
        fields= "__all__"