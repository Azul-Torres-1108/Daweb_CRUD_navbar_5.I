from django.urls import path
from ventas_app import views  # Importamos las vistas desde ventas_app

urlpatterns = [
    path('ventas', views.inicio_vistaVentas, name='ventas'),  # La vista principal que muestra todas las ventas
    path('registrarVenta/', views.registrarVenta, name='registrarVenta'),  # Vista para registrar una nueva venta
    path('borrarVenta/<str:ID_Venta>/', views.borrarVenta, name='borrarVenta'),  # Vista para borrar una venta
    path('seleccionarVenta/<str:ID_Venta>/', views.seleccionarVenta, name='seleccionarVenta'),  # Vista para seleccionar una venta para editar
    path('editarVenta/', views.editarVenta, name='editarVenta'),  # Vista para editar una venta
]

