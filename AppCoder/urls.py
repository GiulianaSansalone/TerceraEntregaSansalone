'''urls de la AppCodder exclusivamente'''
from django.urls import path
from AppCoder.views import index, class_, student, professor, homework, search_class


urlpatterns = [
    path('inicio/', index, name="Inicio"),
    path('cursos/', class_, name="Cursos"),
    path('alumnos/', student, name="Alumnos"),
    path('profesores/', professor, name="Profesores"),
    path('tareas/', homework, name="Tareas"),
    path('buscar_curso/', search_class, name="BuscarCurso")
]
