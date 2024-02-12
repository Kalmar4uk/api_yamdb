from django.db.models import (
    Model, CASCADE, CharField, SlugField, ForeignKey, DateTimeField
)

from reviews.models import User
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


class CommentsReviewModel(Model):
    text = CharField(
        max_length=LEN_FIELD['MAX_LEN_TEXT_REW_COM']
    )
    author = ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name='автор'
    )
    pub_date = DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True
        ordering = ('text',)

    def __str__(self):
        return self.text[:MAX_LEN_LEAD]
