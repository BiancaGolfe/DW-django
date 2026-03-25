from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Estudante, Curso, Matricula

admin.site.register(Estudante)
admin.site.register(Curso)
admin.site.register(Matricula)