from django.test import TestCase
from .models import Author 


class AuthorTestCase(TestCase):
    def setUp(self):
        self.Author =Author.objects.create(name="Akira toriyama")

    def test_is_correct_instance(self):
        self.assertIsInstance(self.Author , Author)


    def test_exists(self):
        author = Author.objects.get( pk = 1 )
        self.assertTrue(author)