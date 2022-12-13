from django.conf import settings
from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):



    @staticmethod
    def setUpClass():
        # The test runner sets DEBUG to False. Set to True to enable SQL logging.
        settings.DEBUG = True
        super(BookSerializerTestCase, BookSerializerTestCase).setUpClass()

    def test_ok(self):
        book1 = Book.objects.create(
            name='Test book1',
            price=30,
            author_name='Test',
        )
        book2 = Book.objects.create(
            name='Test book2',
            price=35,
            author_name='Test',
        )
        data = BookSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'name': 'Test book1',
                'price': '30.00',
                'author_name': 'Test',
            },
            {
                'id': book2.id,
                'name': 'Test book2',
                'price': '35.00',
                'author_name': 'Test',
            }
        ]
        self.assertEqual(expected_data, data)
