from django.db import models

# Create your models here.
from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudante} - {self.curso}"