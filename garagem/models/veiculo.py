

from django.db import models

from garagem.models import Acessorio, Cor, Modelo
from uploader.models import Image


class Veiculo(models.Model):
    # marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    # categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
        )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    # modelo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    acessorio = models.ManyToManyField(Acessorio, related_name="veículos")
    capa = models.ManyToManyField(
        Image,
        related_name="+",
    )

    def __str__(self):
        return f"Modelo: {self.modelo} (Cor: {self.cor} - Ano: {self.ano})"

    class Meta:
        verbose_name = "veículo"