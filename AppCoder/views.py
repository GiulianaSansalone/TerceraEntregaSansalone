from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here

def vista1(request):
    return HttpResponse('iniciando proyecto')


def test_template(self):
    nom = 'Giuliana'
    ap = 'Sansalone'
    diccionario = {'nombre': nom, 'apellido': ap}
    plantilla = loader.get_template("index.html")
    doc = plantilla.render(diccionario)
    return HttpResponse(doc)
