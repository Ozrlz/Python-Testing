from unittest import TestCase

from app import app


class TestHome(TestCase):

    def test_home(self):
        with app.test_client() as client:
            response = client.get('/')
