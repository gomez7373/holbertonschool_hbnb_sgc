import unittest
from models.place import Place
from uuid import uuid4

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        host_id = str(uuid4())
        city_id = str(uuid4())
        amenity_ids = [str(uuid4()), str(uuid4())]
        place = Place(name="SGC's Paradise", description="A beautiful place full of wonders and nature", number_of_rooms=3, number_of_bathrooms=2, max_guests=6, price_per_night=250.0, latitude=-3.465305, longitude=-62.215881, host_id=host_id, city_id=city_id, amenity_ids=amenity_ids)
        self.assertIsNotNone(place.id)
        self.assertEqual(place.name, "SGC's Paradise")
        self.assertEqual(place.description, "A beautiful place full of wonders and nature")
        self.assertEqual(place.number_of_rooms, 3)
        self.assertEqual(place.number_of_bathrooms, 2)
        self.assertEqual(place.max_guests, 6)
        self.assertEqual(place.price_per_night, 250.0)
        self.assertEqual(place.latitude, -3.465305)
        self.assertEqual(place.longitude, -62.215881)
        self.assertEqual(place.host_id, host_id)
        self.assertEqual(place.city_id, city_id)
        self.assertEqual(place.amenity_ids, amenity_ids)

    def test_place_to_dict(self):
        host_id = str(uuid4())
        city_id = str(uuid4())
        amenity_ids = [str(uuid4()), str(uuid4())]
        place = Place(name="SGC's Paradise", description="A beautiful place full of wonders and nature", number_of_rooms=3, number_of_bathrooms=2, max_guests=6, price_per_night=250.0, latitude=-3.465305, longitude=-62.215881, host_id=host_id, city_id=city_id, amenity_ids=amenity_ids)
        place_dict = place.to_dict()
        self.assertEqual(place_dict['name'], "SGC's Paradise")
        self.assertEqual(place_dict['description'], "A beautiful place full of wonders and nature")
        self.assertEqual(place_dict['number_of_rooms'], 3)
        self.assertEqual(place_dict['number_of_bathrooms'], 2)
        self.assertEqual(place_dict['max_guests'], 6)
        self.assertEqual(place_dict['price_per_night'], 250.0)
        self.assertEqual(place_dict['latitude'], -3.465305)
        self.assertEqual(place_dict['longitude'], -62.215881)
        self.assertEqual(place_dict['host_id'], host_id)
        self.assertEqual(place_dict['city_id'], city_id)
        self.assertEqual(place_dict['amenity_ids'], amenity_ids)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)

if __name__ == '__main__':
    unittest.main()
