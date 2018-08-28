from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
import pdb
from functools import wraps
import sys
import traceback

def debug_on(*exceptions):
    if not exceptions:
        exceptions = (AssertionError,)
    def decorator(callback):
        @wraps(callback)
        def wrapper(*args, **kwargs):
            try:
                return callback(*args, **kwargs)
            except exceptions:
                info = sys.exc_info()
                traceback.print_exception(*info)
                pdb.post_mortem(info[2])
        return wrapper
    return decorator

class TestApp(TestCase):

    def setUp(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {blog.title: blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test title', 'Test author', 'q')
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                app.menu()
                mocked_ask_create_blog.assert_called_once()

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', 'Test', 'q')
            with patch('app.ask_read_blog') as mocked_ask_create_blog:
                app.menu()
                mocked_ask_create_blog.assert_called_once()

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'Test title', 'Test author', 'q')
            with patch('app.ask_create_post') as mocked_ask_create_blog:
                app.menu()
                mocked_ask_create_blog.assert_called_once()

    def test_menu_prints_prompt(self):
        ''' This tests if the input func was called with the that arg '''
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)


    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test author (0 posts)')

    def test_ask_create_blog(self):
        TITLE = 'Test'
        AUTHOR = 'Test author'
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = (TITLE, AUTHOR)
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get(TITLE))

    def test_ask_read_blog(self):
        TITLE = 'Test'
        AUTHOR = 'Test author'
        app.blogs[TITLE] = Blog(TITLE, AUTHOR)
        with patch('builtins.input', return_value=TITLE) as mocked_input:
            with patch('blog.Blog.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                
                mocked_print_posts.assert_called_once()


    @debug_on(IndexError)
    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test title', 'Test content')
            app.ask_create_post()

            self.assertEqual(app.blogs.get('Test').posts[0].title, 'Test title')
            self.assertEqual(app.blogs.get('Test').posts[0].content, 'Test content')
            