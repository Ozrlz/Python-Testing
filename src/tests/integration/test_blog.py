from unittest import TestCase
from unittest.mock import patch

from blog import Blog
from post import Post

class TestBlog(TestCase):

    def test_add_post_2_blog(self):
        blog = Blog('Test', 'Test author')
        blog.create_post('Test post', 'Test content')

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, 'Test post')
        self.assertEqual(blog.posts[0].content, 'Test content')

    def test_json(self):
        blog = Blog('Test', 'Test author')
        blog.create_post('Test post', 'Test content')
        
        expexted = {
            'title': 'Test',
            'author': 'Test author',
            'posts': [
                {
                    'title': 'Test post',
                    'content': 'Test content',
                },
            ],
        }

        self.assertDictEqual(expexted, blog.json())

    def test_json_no_posts(self):
        blog = Blog('Test', 'Test author')
        
        expexted = {
            'title': 'Test',
            'author': 'Test author',
            'posts': [
            ],
        }

        self.assertDictEqual(expexted, blog.json())

    def test_print_posts(self):
        blog = Blog('Test', 'Test author')
        blog.create_post('Test post', 'Test content')
        with patch('post.Post.print_post') as mocked_print_post:
            blog.print_posts()
            mocked_print_post.assert_called_once()