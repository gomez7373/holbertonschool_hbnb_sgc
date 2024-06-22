import unittest
from models.city import City
from uuid import uuid4

class TestCity(unittest.TestCase):
    def test_city_creation(self):
        country_code = "BR"  # Brazil, as the Amazon is mostly located there
        city = City(name="Manaus", country_code=country_code)
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "Manaus")
        self.assertEqual(city.country_code, country_code)

    def test_city_to_dict(self):
        country_code = "BR"
        city = City(name="Manaus", country_code=country_code)
        city_dict = city.to_dict()
        self.assertEqual(city_dict['name'], "Manaus")
        self.assertEqual(city_dict['country_code'], country_code)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)

if __name__ == '__main__':
    unittest.main()
