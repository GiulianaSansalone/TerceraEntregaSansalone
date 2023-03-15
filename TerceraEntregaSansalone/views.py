from django.http import HttpResponse
from django.template import Template, Context, loader


def vista1(request):
    return HttpResponse('iniciando proyecto')


def test_template(self):
    nom = 'Giuliana'
    ap = 'Sansalone'
    diccionario = {'nombre': nom, 'apellido': ap}
    plantilla = loader.get_template('template_1.html')
    doc = plantilla.render(diccionario)
    return HttpResponse(doc)
