from django.urls import path
from Entrega_3 import views

urlpatterns = [
    
    path('index/', views.index),
    path('clientes/', views.clientes),
    path('productos/', views.productos),
]

