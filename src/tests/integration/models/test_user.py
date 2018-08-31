from tests.integration.integration_base_test import IntegrationBaseTest
from models.user import UserModel

class TestUser(IntegrationBaseTest):

    def setUp(self):
        self.user = UserModel('username', 'password')
        return super(TestUser, self).setUp()

    def test_save_to_db(self):
        with self.app_context():
            self.assertIsNone(UserModel.find_by_username(self.user.username))
            self.assertIsNone(UserModel.find_by_id(1))

            self.user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username(self.user.username))
            self.assertIsNotNone(UserModel.find_by_id(1))
            