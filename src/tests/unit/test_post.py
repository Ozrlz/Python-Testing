from unittest import TestCase
from unittest.mock import patch

from post import Post
from post import POST_TEMPLATE


class TestPost(TestCase):
    
    def test_create_post(self):
        post = Post('Test', 'Test Content')

        self.assertEqual('Test', post.title)
        self.assertEqual('Test Content', post.content)
    
    def test_json(self):
        post = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, post.json())

    def test_print_post(self):
        post = Post('Test', 'Test Content')
        with patch('builtins.print') as mocked_print:
            post.print_post()
            mocked_print.assert_called_with(
                POST_TEMPLATE.format(post.title, post.content)
            )