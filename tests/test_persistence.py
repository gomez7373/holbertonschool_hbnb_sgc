import unittest
import os
from models.user import User
from models.place import Place
from persistence.data_manager import DataManager

class TestPersistence(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager.instance()
        self.test_file = 'test_data/test_data.json'
        self.data_manager.data = {'User': {}, 'Place': {}, 'City': {}, 'Country': {}, 'Review': {}, 'Amenity': {}}
        self.data_manager.save_data()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_persistence(self):
        user = User(email="sheila.holberton@example.com", first_name="Sheila", last_name="Gomez")
        self.data_manager.save(user)
        self.data_manager.save_data()
        self.data_manager.load_data()
        retrieved_user = self.data_manager.get(user.id, 'User')
        print(f"Retrieved user: {retrieved_user.to_dict() if retrieved_user else None}")
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "sheila.holberton@example.com")

    def test_place_persistence(self):
        place = Place(
            host_id="123", name="SGC's Paradise", description="A beautiful place full of wonders and nature",
            number_of_rooms=3, number_of_bathrooms=2, max_guests=6, price_per_night=250.0,
            latitude=-3.465305, longitude=-62.215881, city_id="456", amenity_ids=["789"]
        )
        self.data_manager.save(place)
        self.data_manager.save_data()
        self.data_manager.load_data()
        retrieved_place = self.data_manager.get(place.id, 'Place')
        print(f"Retrieved place: {retrieved_place.to_dict() if retrieved_place else None}")
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_place.name, "SGC's Paradise")

if __name__ == '__main__':
    unittest.main()
