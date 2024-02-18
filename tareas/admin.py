from django.contrib import admin

from tareas.models import Tareas


# Register your models here.

@admin.register(Tareas)
class tareasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'descripcion',
        'estado'
    )
    list_display_links = ('id',)
