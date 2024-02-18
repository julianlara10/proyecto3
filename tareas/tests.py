from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tareas


class TareasViewSetTestCase(APITestCase):

    def setUp(self):
        self.Tareas = Tareas.objects.create(titulo='Tarea uno', descripcion='Esta es la tarea uno')
        self.url = reverse('Tareas-list')

    def test_listar_Tareas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_obtener_un_Tareas(self):
        url_un_Tareas = reverse('Tareas-detail', args=[self.Tareas.id])
        response = self.client.get(url_un_Tareas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_un_Tareas(self):
        data = {'titulo': 'Tarea dos', 'descripcion': 'Esta es la tarea dos'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_actualizar_un_Tareas(self):
        url_un_Tareas = reverse('Tareas-detail', args=[self.Tareas.id])
        data = {'estado': 'en_progreso'}
        response = self.client.put(url_un_Tareas, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_eliminar_un_Tareas(self):
        url_un_Tareas = reverse('Tareas-detail', args=[self.Tareas.id])
        response = self.client.delete(url_un_Tareas)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

