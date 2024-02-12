from rest_framework import serializers

import api.serializers


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, obj):
        serializer = api.serializers.CategorySerializer(obj)
        return serializer.data


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, obj):
        serializer = api.serializers.GenreSerializer(obj)
        return serializer.data
