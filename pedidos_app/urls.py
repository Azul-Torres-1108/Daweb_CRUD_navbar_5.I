from django.urls import path
from pedidos_app import views  

urlpatterns = [
    path('pedidos', views.inicio_vistaPedidos, name='pedidos'),  # La vista principal
    path('registrarPedido/', views.registrarPedido, name='registrarPedido'),
    path('borrarPedido/<idpedido>/', views.borrarPedido, name='borrarPedido'),
    path('seleccionarPedido/<idpedido>/', views.seleccionarPedido, name='seleccionarPedido'),
    path('editarPedido/', views.editarPedido, name='editarPedido')
]
