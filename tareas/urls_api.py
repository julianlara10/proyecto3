from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tareas.viewsets import TareasViewset

router = DefaultRouter()
router.register('tareas', TareasViewset)


urlpatterns = [
    path('', include(router.urls)),
]