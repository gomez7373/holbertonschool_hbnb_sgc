import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="WiFi")
        self.assertIsNotNone(amenity.id)
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_to_dict(self):
        amenity = Amenity(name="WiFi")
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "WiFi")
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

if __name__ == '__main__':
    unittest.main()
