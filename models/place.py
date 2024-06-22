from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, host_id, name, description, number_of_rooms, number_of_bathrooms, max_guests, price_per_night, latitude, longitude, city_id, amenity_ids, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.host_id = host_id
        self.name = name
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenity_ids = amenity_ids

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict.update({
            'host_id': self.host_id,
            'name': self.name,
            'description': self.description,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'max_guests': self.max_guests,
            'price_per_night': self.price_per_night,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'city_id': self.city_id,
            'amenity_ids': self.amenity_ids
        })
        return place_dict
