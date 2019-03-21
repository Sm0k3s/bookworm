from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, BookCategory


class UserBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
            'url',
            'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = UserBookSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'books')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=BookCategory.objects.all(),
        slug_field='name')

    class Meta:
        model = Book
        fields = (
            'url',
            'title',
            'author',
            'synopsis',
            'category',
            'publishing_date',
            'read')


class BookCategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title')

    class Meta:
        model = BookCategory
        fields = (
            'url',
            'name',
            'books')
