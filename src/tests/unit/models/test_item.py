from tests.unit.unit_test_base import UnitTestBase

from models.item import ItemModel

class TestItem(UnitTestBase):

    def setUp(self):
        self.item = ItemModel('Test name', 123.123, 1)

    def test_create_item(self):
        self.assertEqual(self.item.name,'Test name' )
        self.assertEqual(self.item.price, 123.123)
        self.assertEqual(self.item.store_id,1)
        self.assertIsNone(self.item.store)

    def test_json(self):
        expected_response = {
            'name': self.item.name,
            'price': self.item.price
        }
        self.assertDictEqual(expected_response,self.item.json())