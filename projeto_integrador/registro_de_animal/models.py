from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tutor(models.Model):
    nome = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.nome.username


class Especie (models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    

class Sexo (models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Porte (models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    

class Raça (models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    idade = models.IntegerField()
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)
    cor = models.CharField(max_length=50)
    foto = models.ImageField()
    porte = models.ForeignKey(Porte, on_delete=models.CASCADE)
    raça = models.ForeignKey(Raça, on_delete=models.CASCADE)
    rga = models.CharField(max_length=50)
    castrado = models.BooleanField()
    anilha = models.CharField(max_length=50)
    chip = models.CharField(max_length=50)
    vacinado = models.BooleanField()
    vermifugado = models.BooleanField()

    def __str__(self):
        return self.name
