from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

def inicio_vistaEmpleados(request):
    losempleados = Empleado.objects.all()
    return render(request, "gestionarEmpleados.html", {"misempleados": losempleados})

def registrarEmpleado(request):
    idempleado = request.POST["txtidempleado"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    puesto = request.POST["txtpuesto"]
    fecha_contratacion = request.POST["txtfechacontratacion"]

    Empleado.objects.create(
        idempleado=idempleado,
        nombre=nombre,
        apellido=apellido,
        correo=correo,
        telefono=telefono,
        puesto=puesto,
        fecha_contratacion=fecha_contratacion,
    )
    return redirect("empleados")

def borrarEmpleado(request, idempleado):
    empleado = get_object_or_404(Empleado, idempleado=idempleado)
    empleado.delete()
    return redirect("empleados")

def seleccionarEmpleado(request, idempleado):
    empleado = get_object_or_404(Empleado, idempleado=idempleado)
    return render(request, "editarEmpleados.html", {"empleado": empleado})

def editarEmpleado(request):
    idempleado = request.POST["txtidempleado"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    puesto = request.POST["txtpuesto"]
    fecha_contratacion = request.POST["txtfechacontratacion"]

    empleado = get_object_or_404(Empleado, idempleado=idempleado)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.correo = correo
    empleado.telefono = telefono
    empleado.puesto = puesto
    empleado.fecha_contratacion = fecha_contratacion
    empleado.save()

    return redirect("empleados")
