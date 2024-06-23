import unittest
from models.amenity import Amenity
from persistence.data_manager import DataManager

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager.instance()
        self.data_manager.data['Amenity'] = {}  # Clear existing data
        self.data_manager.save_data()

    def test_amenity_creation(self):
        amenity = Amenity(name="WiFi")
        amenity.save()
        self.assertIsNotNone(amenity.id)
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_to_dict(self):
        amenity = Amenity(name="WiFi")
        amenity.save()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "WiFi")
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

    def test_multiple_amenities(self):
        amenity1 = Amenity(name="WiFi")
        amenity2 = Amenity(name="Pool")
        amenity1.save()
        amenity2.save()

        self.assertIn(amenity1.id, self.data_manager.data['Amenity'])
        self.assertIn(amenity2.id, self.data_manager.data['Amenity'])

if __name__ == '__main__':
    unittest.main()
