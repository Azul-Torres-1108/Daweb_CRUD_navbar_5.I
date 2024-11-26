from django.urls import path
from app_base import views

urlpatterns = [
    # Inicio Tienda artistica
    path('', views.inicio),
]

