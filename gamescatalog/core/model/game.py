from django.db import models


class Jogo(models.Model):
    id = models.AutoField('Código', primary_key=True)
    titulo = models.CharField('Título', max_length=100)


class Plataforma(models.Model):
    titulo = models.CharField('Nome', max_length=100)
    plataforma_jogo = models.ManyToManyField(
        Jogo,
        through='PlataformaJogo',
        through_fields=('plataforma','jogo')
    )


class PlataformaJogo(models.Model):
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

