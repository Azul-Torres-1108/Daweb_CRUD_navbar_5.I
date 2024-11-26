from django.urls import path
from Productos_app import views  

urlpatterns = [
    path('productos', views.inicio_vistaProductos, name='productos'),  # La vista principal
    path('registrarProductos/', views.registrarProductos, name='registrarProductos'),
    path('borrarProductos/<ID_Productos>/', views.borrarProductos, name='borrarProductos'),
    path('seleccionarProductos/<ID_Productos>/', views.seleccionarProductos, name='seleccionarProductos'),
    path('editarProductos/', views.editarProductos, name='editarProductos')
    
]
