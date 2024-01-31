from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, related_name='titles'
    )
    category = models.OneToOneField(
        Category, on_delete=models.SET_NULL, null=True, related_name='titles'
    )

    def __str__(self):
        return self.name
