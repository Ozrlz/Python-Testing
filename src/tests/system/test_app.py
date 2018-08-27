from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class TestApp(TestCase):

    def test_print_blogs(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {blog.title: blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test author (0 posts)')