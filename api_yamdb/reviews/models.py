from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from reviews.constants import (
    ADMIN, LEN_FIELD, MAX_LEN_LEAD, MODERATOR, USER, USER_ROLES
)
from reviews.validators import (
    validate_correct_username,
    validate_username,
    validate_year
)


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Никнэйм пользователя',
        validators=[validate_correct_username, validate_username],
        max_length=LEN_FIELD['MAX_LEN_USERNAME'],
        unique=True,
    )

    email = models.EmailField(
        verbose_name='Почта пользователя',
        max_length=LEN_FIELD['MAX_LEN_EMAIL'],
        unique=True,
        null=False
    )
    role = models.CharField(
        verbose_name='Пользовательская роль',
        max_length=LEN_FIELD['MAX_LEN_ROLE'],
        choices=USER_ROLES,
        default=USER,
        blank=True
    )
    bio = models.TextField(
        verbose_name='Биография пользователя',
        blank=True
    )

    @property
    def is_admin(self):
        return (
            self.role == ADMIN
            or self.is_staff
            or self.is_superuser
        )

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username


import core.abstract_models


class Genre(core.abstract_models.CatogoryGenreModel):

    class Meta(core.abstract_models.CatogoryGenreModel.Meta):
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(core.abstract_models.CatogoryGenreModel):

    class Meta(core.abstract_models.CatogoryGenreModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Title(models.Model):
    name = models.CharField(
        'Название',
        max_length=LEN_FIELD['MAX_LEN_NAME_TIT_CAT_GEN']
    )
    year = models.SmallIntegerField('Год', validators=[validate_year])
    description = models.TextField('Описание', null=True, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр(-ы)')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='titles',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Проиведения'
        ordering = ('year',)

    def __str__(self):
        return self.name[:MAX_LEN_LEAD]


class Review(core.abstract_models.CommentsReviewModel):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='произведение'
    )
    text = models.CharField(
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='автор'
    )
    score = models.IntegerField(
        'оценка',
        validators=(
            MinValueValidator(LEN_FIELD['MIN_VALUE_VALID']),
            MaxValueValidator(LEN_FIELD['MAX_VALUE_VALID'])
        ),
        error_messages={
            'validators':
            f'Оценка от {LEN_FIELD["MIN_VALUE_VALID"]} '
            f'до {LEN_FIELD["MAX_VALUE_VALID"]}!'
        }
    )

    class Meta:
        default_related_name = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author', ),
                name='unique review'
            )]
        ordering = ('pub_date',)

    def str(self):
        return self.text

class Comment(core.abstract_models.CommentsReviewModel):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='отзыв'
    )

    class Meta(core.abstract_models.CommentsReviewModel.Meta):
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def str(self):
        return self.text
