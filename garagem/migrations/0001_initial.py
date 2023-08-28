# Generated by Django 4.2.4 on 2023-08-28 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Acessorio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "acessório",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Cor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descricao", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "cores",
            },
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                (
                    "nacionalidade",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Veiculo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                    ),
                ),
                ("modelo", models.CharField(max_length=50)),
                (
                    "acessorio",
                    models.ManyToManyField(
                        related_name="veículos", to="garagem.acessorio"
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="garagem.categoria",
                    ),
                ),
                (
                    "cor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="garagem.cor",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="veiculos",
                        to="garagem.marca",
                    ),
                ),
            ],
            options={
                "verbose_name": "veículo",
            },
        ),
    ]
