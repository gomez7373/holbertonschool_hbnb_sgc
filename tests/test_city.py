import unittest
from models.city import City
from persistence.data_manager import DataManager

class TestCity(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager.instance()
        self.data_manager.data['City'] = {}  # Clear existing data
        self.data_manager.save_data()

    def test_city_creation(self):
        city = City(name="Manaus", country_code="BR")
        city.save()
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "Manaus")
        self.assertEqual(city.country_code, "BR")

    def test_city_to_dict(self):
        city = City(name="Manaus", country_code="BR")
        city.save()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['name'], "Manaus")
        self.assertEqual(city_dict['country_code'], "BR")
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)

    def test_multiple_cities(self):
        city1 = City(name="Manaus", country_code="BR")
        city2 = City(name="Rio de Janeiro", country_code="BR")
        city1.save()
        city2.save()

        self.assertIn(city1.id, self.data_manager.data['City'])
        self.assertIn(city2.id, self.data_manager.data['City'])

if __name__ == '__main__':
    unittest.main()
