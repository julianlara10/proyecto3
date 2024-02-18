# **PROYECTO 3**

Este es un proyecto básico de Django con una aplicación proyecto 3, correspondiente a la prueba de SERVINFORMACION.

## Clonar Proyecto

Lo primero que se debe hacer es clonar el proyecto del repositorio fuente

## Configurar el entorno virtual

Para correr el proyecto es opcional configurar un entorno virtual, esta configuracion es a gusto del usuario de acuerdo al sistema operativo o entorno de su preferencia

## Instalar requerimientos

Una vez clonado el proyecto debemos instalar todos los requerimientos necesarios para la correcta ejecucion del proyecto por lo cual debemos ingresr desde la ruta principal el siguiente comando:

```python
pip install -r requirements.txt
```

## Aplicar migraciones

Antes de poner en ejecucion, debemos aplicar migraciones las cuales se aplican con la ejecucion del siguiente comando:

```python
python manage.py migrate
```

## Crear superusuario

Para poder acceder al proyecto y sus funcionalidades, es necesario de un usuario, por lo cual debe crearse mediante el siguiente comando: 

```python
python manage.py createsuperuser
```

De igual manera el usuario creado previamente es:

** Usuario: ** *admin*
** Contraseña: ** *admin2024*

## Correr el proyecto

Una vez instalados los requerimientos del proyecto, para ponerlo en ejecucion debemos ejecutar desde consola el siguiente comando:

```python
python manage.py runserver
```

Una vez este en ejecucion podremos acceder al sitio administrador o al endpoints requerido

** Los enlaces de acceso son los siguientes: **

- http://localhost:8000/admin/                          **Sitio de administracion** 
- http://localhost:8000/tareas/                          **Endpoint de tareas**

## ** Como usar la API **

El ejercicio requiere que los usuarios puedan: 

- Crear una nueva tarea.
- Obtener la lista de todas las tareas.
- Obtener detalles de una tarea específica.
- Actualizar el estado de una tarea (pendiente, en progreso, completada).
- Eliminar una tarea.


** A continuacion se explica como lograr cada uno de los requerimientos **

#### Crear una nueva tarea. ####

Para crear una nueva tarea debemos hacer una solicitud HTTP con metodo **POST** al enlace http://localhost:8000/tareas/, en autenticacion debemos enviar *usuario* y *contraseña* y como body debemos enviar los paramentros obligatorios

- titulo
- descripcion
 y el parametro estado como estado opcional, los unicos valores permitidos para el campo estado son: *pendiente*, *en_progreso* y *completada*

#### Obtener la lista de todas las tareas. ####

Para obtener todas las tareas debemos hacer una solicitud HTTP con metodo **GET** al enlace http://localhost:8000/tareas/, unicamente debemos enviar en autenticacion *usuario* y *contraseña* 

#### Obtener detalles de una tarea específica. ####

Para obtener el detalle de una tarea en especifico debemos hacer una solicitud HTTP con metodo **GET** al enlace http://localhost:8000/tareas/{id}/, debemos enviar en autenticacion *usuario* y *contraseña* y debemos en la url espcificar el id de la tarea

un ejemplo seria: http://localhost:8000/tareas/5/

#### Actualizar el estado de una tarea. ####

Para actulizar el estado de una tarea debemos hacer una solicitud HTTP con metodo **PATCH** al enlace http://localhost:8000/tareas/{id}, en autenticacion debemos enviar *usuario* y *contraseña*, debemos especificar en la url el id de la tarea a actualizar
y como body debemos enviar el parametro de estado con su respectivo valor permitido

los unicos valores permitidos para el campo estado son: *pendiente*, *en_progreso* y *completada*

un ejemplo seria: http://localhost:8000/tareas/5/

#### Eliminar una tarea. ####

Para eliminar una tarea en especifico debemos hacer una solicitud HTTP con metodo **DELETE** al enlace http://localhost:8000/tareas/{id}/, debemos enviar en autenticacion *usuario* y *contraseña* y debemos en la url espcificar el id de la tarea

un ejemplo seria: http://localhost:8000/tareas/5/



#### Dentro del repositorio se encuentra un fixture de la base de datos, se encuentra un exportado del repositorio en postman, y un archivo de texto con los requerimientos necesarios
