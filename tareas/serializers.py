from rest_framework import serializers

from tareas.models import Tareas
from tareas.utils import ESTADO


class TareasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tareas
        fields = '__all__'

    def validate_estado(self, value):

        choices_estado = dict(ESTADO)

        if value not in choices_estado:
            raise serializers.ValidationError(f'El estado debe ser uno de: {list(choices_estado.keys())}')
        return value
