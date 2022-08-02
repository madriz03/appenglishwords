from django.db import models
from django.contrib.auth.models import User
#importamos la clase user para q nos cree un modelo o tabla preseterminado de usuarios

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #se declara el user como la fk que lleva como parametro la clase User importada que es un modelo por default.
    word = models.CharField(max_length=200, null=True, blank=True)
    translation = models.CharField(max_length=200, null=True, blank=True)
    sentence = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.word

    class Meta:
        ordering = ['complete']
#Esta clase es para ordenar los objetos segun lo q muestre la variable complete