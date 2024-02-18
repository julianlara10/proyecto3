from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tareas.models import Tareas
from tareas.serializers import TareasSerializer


class TareasViewset(viewsets.ModelViewSet):

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post', 'delete', 'patch')
    ordering = ('pk',)
    ordering_fields = ('pk',)

