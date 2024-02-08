from datetime import datetime as dt

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, User
from reviews.validators import validate_correct_username, validate_username


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        lookup_field = 'username'


class UserMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        lookup_field = 'username'
        read_only_fields = ('role',)


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[validate_correct_username, validate_username]
    )
    email = serializers.EmailField(
        required=True,
        max_length=254
    )

    class Meta:
        model = User
        lookup_field = 'username'
        fields = ('email', 'username')


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = '__all__'

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка по 10-бальной шкале!')
        return value

    def validate(self, data):
        request = self.context['request']
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and Review.objects.filter(title=title).exists()
        ):
            raise ValidationError('Может существовать только один отзыв!')
        return data


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ('id',)


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, obj):
        serializer = CategorySerializer(obj)
        return serializer.data


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, obj):
        serializer = GenreSerializer(obj)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    category = CategoryField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = GenreField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )

    def validate_year(self, value):
        if dt.now().year < value:
            raise serializers.ValidationError(
                'Год произведения не может быть больше текущего.'
            )
        return value
