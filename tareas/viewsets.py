from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tareas.models import Tareas
from tareas.serializers import TareasSerializer


class TareasViewset(viewsets.ModelViewSet):

    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post', 'delete', 'patch')
    ordering = ('pk',)
    ordering_fields = ('pk',)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(
                queryset,
                many=True,
                context={
                    'request': request,
                }
            )
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            tarea = self.get_object()
            return Response(self.serializer_class(tarea).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = TareasSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            tarea = self.get_object()
            serializer = self.get_serializer(tarea, data=request.data, partial=True)
            if serializer.is_valid():
                tarea.estado = serializer.validated_data['estado']
                tarea.save()
                # serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Unicamente debe actualizarse el campo estado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            tarea = self.get_object()
            tarea.delete()
            return Response('Tarea eliminada Correctamente')
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
