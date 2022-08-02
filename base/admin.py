from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)

#Se debe agregar para poder ver nuestro modelo en el administrador de django