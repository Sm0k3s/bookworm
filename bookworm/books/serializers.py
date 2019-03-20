from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Book, BookCategory


class BookSerializer(serializers.HyperlinkedModelSerializer):
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
    class Meta:
        model = BookCategory
        fields = (
            'url',
            'name')
