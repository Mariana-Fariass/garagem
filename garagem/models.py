from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Acessorio"
        verbose_name_plural = "Acessórios"