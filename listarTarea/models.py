from django.db import models

# Create your models here.

class Tarea(models.Model):
    ESTADO_CHOISES=[
        ('completado','Completado'),
        ('pendiente','Pendiente')
    ]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    completado = models.CharField(max_length=100, choices= ESTADO_CHOISES )

    def __str__(self):
        return self.titulo

