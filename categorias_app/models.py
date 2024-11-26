from django.db import models

# Create your models here.

class Categoria(models.Model):
    idcategoria = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=100)  
    orden = models.IntegerField()
    marca = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
