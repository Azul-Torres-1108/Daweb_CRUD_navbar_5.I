from django.db import models

class Empleado(models.Model):
    idempleado = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    puesto = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre
