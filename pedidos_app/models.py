from django.db import models

# Create your models here.

class Pedido(models.Model):
    idpedido = models.CharField(primary_key=True, max_length=6)
    idcliente = models.PositiveSmallIntegerField(max_length=6)
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=255) 
    total = models.DecimalField(max_digits=10, decimal_places=2) 
    metodopago = models.CharField(max_length=50)
    direccion_envio = models.CharField(max_length=100)

    def __str__(self):
        return self.idpedido
