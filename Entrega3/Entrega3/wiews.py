from django.http import HttpResponse
from django.template import loader, Context, Template
from django.shortcuts import render

def probandoPlantillas(req, name):
    plantilla = loader.get_template('index.html')
    documento = plantilla.render({    
        'titulo': 'Mi primera página en Django',
        'contenido': 'Hola ' + name
    })

    return HttpResponse(documento)
