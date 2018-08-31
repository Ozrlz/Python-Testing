from models.store import StoreModel
from tests.unit.unit_test_base import UnitTestBase

class TestStore(UnitTestBase):

    def test_create_store(self):
        store = StoreModel('Test name')
        self.assertEqual(store.name, 'Test name')