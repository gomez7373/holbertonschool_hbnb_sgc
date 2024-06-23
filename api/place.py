from flask import Blueprint, request, jsonify
from models.place import Place

place_bp = Blueprint('place_bp', __name__)

@place_bp.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    place = Place(
        host_id=data.get('host_id'),
        name=data.get('name'),
        description=data.get('description'),
        number_of_rooms=data.get('number_of_rooms'),
        number_of_bathrooms=data.get('number_of_bathrooms'),
        max_guests=data.get('max_guests'),
        price_per_night=data.get('price_per_night'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        city_id=data.get('city_id'),
        amenity_ids=data.get('amenity_ids', [])
    )
    place.save()
    return jsonify(place.to_dict()), 201

@place_bp.route('/places', methods=['GET'])
def get_places():
    places = Place.persistence.data['Place'].values()
    places_list = [place.to_dict() for place in places]
    return jsonify(places_list), 200

@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.persistence.get(place_id, 'Place')
    if place:
        return jsonify(place.to_dict()), 200
    return jsonify({'error': 'Place not found'}), 404

@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = Place.persistence.get(place_id, 'Place')
    if place:
        place.host_id = data.get('host_id', place.host_id)
        place.name = data.get('name', place.name)
        place.description = data.get('description', place.description)
        place.number_of_rooms = data.get('number_of_rooms', place.number_of_rooms)
        place.number_of_bathrooms = data.get('number_of_bathrooms', place.number_of_bathrooms)
        place.max_guests = data.get('max_guests', place.max_guests)
        place.price_per_night = data.get('price_per_night', place.price_per_night)
        place.latitude = data.get('latitude', place.latitude)
        place.longitude = data.get('longitude', place.longitude)
        place.city_id = data.get('city_id', place.city_id)
        place.amenity_ids = data.get('amenity_ids', place.amenity_ids)
        place.save()
        return jsonify(place.to_dict()), 200
    return jsonify({'error': 'Place not found'}), 404

@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Place.persistence.get(place_id, 'Place')
    if place:
        place.delete()
        return jsonify({'success': 'Place deleted'}), 200
    return jsonify({'error': 'Place not found'}), 404
