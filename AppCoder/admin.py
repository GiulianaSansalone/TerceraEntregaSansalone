from django.contrib import admin
from .models import Class, Student, Professor, Homework
# Register your models here.
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Homework)