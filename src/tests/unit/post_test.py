from unittest import TestCase
from post import Post

class PostTest(TestCase):
    
    def test_create_post(self):
        post = Post('Test', 'Test Content')

        self.assertEqual('Test', post.title)
        self.assertEqual('Test Content', post.content)
