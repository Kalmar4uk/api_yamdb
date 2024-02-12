from django.db import models

from reviews.constants import LEN_FIELD, MAX_LEN_LEAD


class CatogoryGenreModel(models.Model):
    name = models.CharField(
        'Название',
        max_length=LEN_FIELD['MAX_LEN_NAME_TIT_CAT_GEN']
    )
    slug = models.SlugField('Слаг', unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name[:MAX_LEN_LEAD]
