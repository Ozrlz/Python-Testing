from tests.integration.integration_base_test import IntegrationBaseTest
from models.store import StoreModel
from models.item import ItemModel

class TestStore(IntegrationBaseTest):

    def setUp(self):
        self.store = StoreModel('Test name')
        return super(TestStore, self).setUp()

    def test_items_is_empty_on_creation(self):
        self.assertListEqual(self.store.items.all(), [])

    def test_save_to_db(self):
        with self.app_context():
            self.assertIsNone(StoreModel.find_by_name('Test name'))
            self.store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('Test name'))

    def test_delete_from_db(self):
        with self.app_context():
            self.assertIsNone(StoreModel.find_by_name('Test name'))
            self.store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('Test name'))
            self.store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('Test name'))

    def test_store_relationship(self):
        with self.app_context():
            self.store.save_to_db()
            item = ItemModel('Test item', 19.99, self.store.id)
            item.save_to_db()

            self.assertEqual(self.store.items.count(), 1)
            self.assertEqual(self.store.items.first().name, 'Test item')

    def test_store_json(self):
        expected = {
            'name': 'Test name',
            'items': [],
        }

        self.assertDictEqual(self.store.json(), expected)

    def test_store_json_with_item(self):
        expected = {
            'name': 'Test name',
            'items': [{
                'name': 'Test item',
                'price': 19.99
            }],
        }
        with self.app_context():
            self.store.save_to_db()
            item = ItemModel('Test item', 19.99, self.store.id)
            item.save_to_db()
            self.assertDictEqual(self.store.json(), expected)