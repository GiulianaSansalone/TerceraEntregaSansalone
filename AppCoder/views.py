from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here
''''Las vistas creadas hasta el momento (terera pre-entrega) 
no realizan ninguna función más que mostrar los templates cargados'''
def classes(request):
    dictionary = dict()
    template = loader.get_template("Classes.html")
    doc = template.render(dictionary)
    return HttpResponse(doc)
def students(request):
    dictionary = dict()
    template = loader.get_template("Students.html")
    doc = template.render(dictionary)
    return HttpResponse(doc)
def professors(request):
    dictionary = dict()
    template = loader.get_template("Professors.html")
    doc = template.render(dictionary)
    return HttpResponse(doc)
def homework(request):
    dictionary = dict()
    template = loader.get_template("Homework.html")
    doc = template.render(dictionary)
    return HttpResponse(doc)

def index(self):
    dictionary = dict()
    template = loader.get_template("index.html")
    doc = template.render(dictionary)
    return HttpResponse(doc)
