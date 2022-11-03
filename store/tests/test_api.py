from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            name='Test book1',
            price=30,
            author_name='Author 1',
        )
        self.book2 = Book.objects.create(
            name='Test book2',
            price=35,
            author_name='Author 5',
        )
        self.book3 = Book.objects.create(
            name='Test book3 Author 1',
            price=35,
            author_name='Author 1',
        )
        self.url = reverse('book-list')

    def test_get(self):
        response = self.client.get(self.url)
        serializer_data = BookSerializer([self.book1, self.book2, self.book3], many=True).data
        self.assertEqual(serializer_data, response.data)

    def test_status(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BookSerializer([self.book1, self.book3], many=True).data
        self.assertEqual(serializer_data, response.data)
