from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido

def inicio_vistaPedidos(request):
    lospedidos = Pedido.objects.all()
    return render(request, "gestionarPedidos.html", {"mispedidos": lospedidos})

def registrarPedido(request):
    idpedido = request.POST["txtidpedido"]
    idcliente = request.POST["txtidcliente"]
    fecha_pedido = request.POST["txtfechapedido"]
    estado = request.POST["txtestado"]
    total = request.POST["numtotal"]  
    metodopago = request.POST["txtmetodopago"]
    direccion_envio = request.POST["txtdireccionenvio"]

    Pedido.objects.create(
        idpedido=idpedido,
        idcliente=idcliente,
        fecha_pedido=fecha_pedido,
        estado=estado,
        total=total,
        metodopago=metodopago,
        direccion_envio=direccion_envio,
    )
    return redirect("pedidos")

def borrarPedido(request, idpedido):
    pedido = get_object_or_404(Pedido, idpedido=idpedido)
    pedido.delete()
    return redirect("pedidos")

def seleccionarPedido(request, idpedido):
    pedido = get_object_or_404(Pedido, idpedido=idpedido)
    return render(request, "editarPedidos.html", {"pedido": pedido})

def editarPedido(request):
    idpedido = request.POST["txtidpedido"]
    idcliente = request.POST["txtidcliente"]
    fecha_pedido = request.POST["txtfechapedido"]
    estado = request.POST["txtestado"]
    total = request.POST["numtotal"]  
    metodopago = request.POST["txtmetodopago"]
    direccion_envio = request.POST["txtdireccionenvio"]

    pedido = get_object_or_404(Pedido, idpedido=idpedido)

    pedido.idcliente = idcliente
    pedido.fecha_pedido = fecha_pedido
    pedido.estado = estado
    pedido.total = total
    pedido.metodopago = metodopago
    pedido. direccion_envio = direccion_envio
    pedido.save()


    return redirect("pedidos")
