from django.urls import path
from Cliente_app import views  

urlpatterns = [
    path('clientes', views.inicio_vistaClientes, name='clientes'),  # La vista principal
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('borrarCliente/<ID_Cliente>/', views.borrarCliente, name='borrarCliente'),
    path('seleccionarCliente/<ID_Cliente>/', views.seleccionarCliente, name='seleccionarCliente'),
    path('editarCliente/', views.editarCliente, name='editarCliente')
    
]
