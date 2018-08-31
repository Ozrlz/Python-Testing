from models.user import UserModel
from tests.unit.unit_test_base import UnitTestBase

class TestUser(UnitTestBase):
    def setUp(self):
        self.user = UserModel('username', 'password')
        return super(TestUser, self).setUp()

    def test_create_user(self):
         self.assertEqual(self.user.username, 'username')
         self.assertEqual(self.user.password, 'password')

    