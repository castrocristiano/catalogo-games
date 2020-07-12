from django.db import models


class Jogo(models.Model):
    id = models.AutoField('Código', primary_key=True)
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho', max_length=50)

    def __str__(self):
        return self.titulo

    class Meta:
        """
            Classe para definições de metadados dos modelos
        """
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['titulo', 'slug', 'id']

