from django.test import TestCase
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BookCategory
# Create your tests here.

class BookCategoryTests(APITestCase):
    def create_book_category(self, name):
        url = reverse('book-categories')
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_create_and_retrieve_book_category(self):
        """
        Ensure we can create a new BookCategory and then retrieve it
        """
        new_category = 'New Category'
        response = self.create_book_category(new_category)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BookCategory.objects.count(), 1)
        self.assertEqual(
            BookCategory.objects.get().name,
            new_category)
        print("PK {0}".format(BookCategory.objects.get().pk))
