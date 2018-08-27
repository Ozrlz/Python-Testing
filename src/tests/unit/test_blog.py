from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_blog(self):
        blog = Blog('Test', 'Test author')

        self.assertEqual('Test', blog.title)
        self.assertEqual('Test author', blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog = Blog('Test', 'Test author')

        self.assertEqual(blog.__repr__(), 'Test by Test author (0 posts)')