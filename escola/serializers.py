from rest_framework import serializers
from .models import Estudante, Curso, Matricula


# 🔹 SERIALIZER DE ESTUDANTE
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

    # Validação do nome
    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value

    # Validação do email
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Email inválido.")
        return value


# 🔹 SERIALIZER DE CURSO
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

    # Validação do nome do curso
    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome do curso deve ter pelo menos 3 caracteres.")
        return value


# 🔹 SERIALIZER DE MATRÍCULA
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

    # Validação geral
    def validate(self, data):
        estudante = data.get('estudante')
        curso = data.get('curso')

        # Evitar matrícula duplicada
        if Matricula.objects.filter(estudante=estudante, curso=curso).exists():
            raise serializers.ValidationError("Este estudante já está matriculado neste curso.")

        return data