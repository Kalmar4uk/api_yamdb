from django.db import models


class CatogoryGenreModel(models.Model):
    name = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name[:10]
