from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Class, Student, Professor, Homework
from AppCoder.forms import ClassForm, StudentForm, ProfessorForm, HomeworkForm

# Create your views here
'''Las vistas creadas hasta el momento (terera pre-entrega) 
no realizan ninguna función más que mostrar los templates cargados'''


def class_(request):
    if request.method == "POST":
        form1 = ClassForm(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            class_save = Class(
                name=info['nombre'],
                commission=info['comisión']
            )
            class_save.save()
    all_classes = Class.objects.all()
    context = {'classes': all_classes,
               'form': ClassForm
               }
    return render(request, 'Classes.html', context=context)


def student(request):
    if request.method == "POST":
        form1 = StudentForm(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            student_save = Student(
                name=info['nombre'],
                surname=info['apellido'],
                mail=info['mail']
            )
            student_save.save()
    all_students = Student.objects.all()
    context = {'students': all_students,
               'form': StudentForm
               }
    return render(request, 'Students.html', context=context)


def professor(request):
    if request.method == "POST":
        form1 = ProfessorForm(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            prof_save = Professor(
                name=info['nombre'],
                surname=info['apellido'],
                mail=info['mail'],
                profession=info['profesión']
            )
            prof_save.save()
    all_prof = Professor.objects.all()
    context = {'professors': all_prof,
               'form': ProfessorForm
               }
    return render(request, 'Professors.html', context=context)



def homework(request):
    if request.method == "POST":
        form1 = HomeworkForm(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            hw_save = Homework(
                name=info['nombre'],
                date=info['fecha'],
                handed_in=info['estado']
            )
            hw_save.save()
    all_hw = Homework.objects.all()
    context = {'homework': all_hw,
               'form': HomeworkForm
               }
    return render(request, 'Homework.html', context=context)



def index(self):
    dictionary = dict()
    template = loader.get_template("index.html")
    doc = template.render(dictionary)
    return HttpResponse(doc)
