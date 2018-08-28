from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class TestApp(TestCase):

    def test_menu_prints_prompt(self):
        ''' This tests if the input func was called with the that arg '''
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {blog.title: blog}
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

