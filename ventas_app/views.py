from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta

def inicio_vistaVentas(request):
    losventas = Venta.objects.all()
    return render(request, "gestionarVentas.html", {"misventas": losventas})

def registrarVenta(request):
    ID_Venta = request.POST["txtID_Venta"]
    ID_Producto = request.POST["txtID_Producto"]
    ID_Cliente = request.POST["txtID_Cliente"]
    Cantidad_vendida = request.POST["txtCantidad_vendida"]
    Precio_Total = request.POST["txtPrecio_Total"]
    Fecha_venta = request.POST["txtFecha_venta"]
    Metodo_Pago = request.POST["txtMetodo_Pago"]

    Venta.objects.create(
        ID_Venta=ID_Venta,
        ID_Producto=ID_Producto,
        ID_Cliente=ID_Cliente,
        Cantidad_vendida=Cantidad_vendida,
        Precio_Total=Precio_Total,
        Fecha_venta=Fecha_venta,
        Metodo_Pago=Metodo_Pago,
    )
    return redirect("ventas")

def borrarVenta(request, ID_Venta):
    venta = get_object_or_404(Venta, ID_Venta=ID_Venta)
    venta.delete()
    return redirect("ventas")

def seleccionarVenta(request, ID_Venta):
    venta = get_object_or_404(Venta, ID_Venta=ID_Venta)
    return render(request, "editarVentas.html", {"venta": venta})

def editarVenta(request):
    ID_Venta = request.POST["txtID_Venta"]
    ID_Producto = request.POST["txtID_Producto"]
    ID_Cliente = request.POST["txtID_Cliente"]
    Cantidad_vendida = request.POST["txtCantidad_vendida"]
    Precio_Total = request.POST["txtPrecio_Total"]
    Fecha_venta = request.POST["txtFecha_venta"]
    Metodo_Pago = request.POST["txtMetodo_Pago"]

    venta = get_object_or_404(Venta, ID_Venta=ID_Venta)

    venta.ID_Venta = ID_Venta
    venta.ID_Producto = ID_Producto
    venta.ID_Cliente = ID_Cliente
    venta.Cantidad_vendida = Cantidad_vendida
    venta.Precio_Total = Precio_Total
    venta.Fecha_venta = Fecha_venta
    venta.Metodo_Pago = Metodo_Pago
    venta.save()

    return redirect("ventas")
