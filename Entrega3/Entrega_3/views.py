from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Entrega_3/index.html")

def clientes(request):
    return HttpResponse("Entrega_3/clientes.html")

def productos(request):
    return HttpResponse("Entrega_3/productos.html")
