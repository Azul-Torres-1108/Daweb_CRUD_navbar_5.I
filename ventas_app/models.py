from django.db import models

# Create your models here.

class Venta(models.Model):
    ID_Venta = models.CharField(primary_key=True, max_length=6)
    ID_Producto = models.CharField(max_length=6)
    ID_Cliente = models.CharField(max_length=6)
    Cantidad_vendida = models.IntegerField()
    Precio_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha_venta = models.DateField()
    Metodo_Pago = models.CharField(max_length=50)

    def __str__(self):
        return self.ID_Venta
