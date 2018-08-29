from tests.system.base_test import BaseTest
import json


class TestHome(BaseTest):

    def test_home_status_code(self):
        with self.app() as client:
            response = client.get('/')
            self.assertEqual(200, response.status_code
            )
    def test_home_response(self):
        with self.app() as client:
            response = client.get('/')
            self.assertEqual(json.loads(response.get_data()),
                                {'message': 'Hello world c:'})
