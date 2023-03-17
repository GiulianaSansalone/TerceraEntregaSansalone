'''urls de la AppCodder exclusivamente'''
from django.urls import path
from AppCoder.views import index, classes, students, professors, homework
urlpatterns = [
    path('inicio/', index, name="Inicio"),
    path('cursos/', classes, name="Cursos"),
    path('alumnos/', students, name="Alumnos"),
    path('profesores/', professors, name="Profesores"),
    path('tareas/', homework, name="Tareas")

]