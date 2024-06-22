import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def test_country_creation(self):
        country = Country(code="BR", name="Brazil")
        self.assertIsNotNone(country.code)
        self.assertEqual(country.name, "Brazil")

    def test_country_to_dict(self):
        country = Country(code="BR", name="Brazil")
        country_dict = country.to_dict()
        self.assertEqual(country_dict['code'], "BR")
        self.assertEqual(country_dict['name'], "Brazil")

if __name__ == '__main__':
    unittest.main()
