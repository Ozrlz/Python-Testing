from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):

    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()
            item = ItemModel('Test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('Test'))
            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Test'))

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('Test'))
            
    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test store')
            item = ItemModel('Test', 19.00, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'Test store')