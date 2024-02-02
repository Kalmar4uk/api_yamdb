from rest_framework import viewsets

from reviews.models import Category, Genre, Title
from .serializers import CategorySerializer, GengreSerializer, TitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']


class GengreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GengreSerializer
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
