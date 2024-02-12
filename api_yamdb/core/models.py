from django.db.models import (
    CharField, Model, SlugField
)

from reviews.constants import LEN_FIELD, MAX_LEN_LEAD


class CatogoryGenreModel(Model):
    name = CharField(
        'Название',
        max_length=LEN_FIELD['MAX_LEN_NAME_TIT_CAT_GEN']
    )
    slug = SlugField('Слаг', unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name[:MAX_LEN_LEAD]
