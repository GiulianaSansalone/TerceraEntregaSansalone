from django import forms


class ClassForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    comisión = forms.IntegerField(min_value=1000)


class StudentForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=30)
    mail = forms.CharField(max_length=30)


class ProfessorForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=30)
    mail = forms.CharField(max_length=30)
    profesión = forms.CharField(min_length=3, max_length=30)


class HomeworkForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha = forms.DateField()
    estado = forms.BooleanField()
