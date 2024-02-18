from django.db import models

from tareas.utils import ESTADO


# Create your models here.

class Tareas(models.Model):
    titulo = models.CharField(
        max_length=254,
        verbose_name='Titulo',
    )
    descripcion = models.TextField(
        max_length=500,
        verbose_name='Descripcion',
    )
    estado = models.CharField(
        max_length=25,
        choices=ESTADO,
        default='pendiente',
        verbose_name='Estado'
    )

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return f'{self.titulo} | {self.estado}'
