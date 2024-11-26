from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria

def inicio_vistaCategorias(request):
    lascategorias = Categoria.objects.all()
    return render(request, "gestionarCategoria.html", {"miscategorias": lascategorias})

def registrarCategoria(request):
    idcategoria = request.POST["txtidcategoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    fecha_creacion = request.POST["txtfechacreacion"]
    estado = request.POST["txtestado"]  
    orden = request.POST["numorden"]
    marca = request.POST["txtmarca"]

    Categoria.objects.create(
        idcategoria=idcategoria,
        nombre=nombre,
        descripcion=descripcion,
        fecha_creacion=fecha_creacion,
        estado=estado,
        orden=orden,
        marca=marca,
    )
    return redirect("categorias")

def borrarCategoria(request, idcategoria):
    categoria = get_object_or_404(Categoria, idcategoria=idcategoria)
    categoria.delete()
    return redirect("categorias")

def seleccionarCategoria(request, idcategoria):
    categoria = get_object_or_404(Categoria, idcategoria=idcategoria)
    return render(request, "editarCategoria.html", {"categoria": categoria})

def editarCategoria(request):
    idcategoria = request.POST["txtidcategoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    fecha_creacion = request.POST["txtfechacreacion"]
    estado = request.POST["txtestado"]  
    orden = request.POST["numorden"]
    marca = request.POST["txtmarca"]

    categoria = get_object_or_404(Categoria, idcategoria=idcategoria)

    categoria.nombre = nombre
    categoria.descripcion = descripcion
    categoria.fecha_creacion = fecha_creacion
    categoria.estado = estado
    categoria.orden = orden
    categoria.marca = marca
    categoria.save()


    return redirect("categorias")
