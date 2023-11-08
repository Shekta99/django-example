from rest_framework import serializers
from rest.models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'nombre', 'completada']