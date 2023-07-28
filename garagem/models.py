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

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    modelo= models.CharField(max_length=50)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} {self.cor} {self.modelo} "
    
    class Meta:
        verbose_name = "veículo"