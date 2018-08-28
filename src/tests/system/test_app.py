from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class TestApp(TestCase):

    def test_menu_prints_prompt(self):
        ''' This tests if the input func was called with the that arg '''
        with patch('builtins.input') as mocked_input:
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
