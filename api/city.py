from flask import Blueprint, request, jsonify
from models.city import City

city_bp = Blueprint('city_bp', __name__)

@city_bp.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    city = City(name=data.get('name'), country_code=data.get('country_code'))
    city.save()
    return jsonify(city.to_dict()), 201

@city_bp.route('/cities', methods=['GET'])
def get_cities():
    cities = City.persistence.data['City'].values()
    cities_list = [city.to_dict() for city in cities]
    return jsonify(cities_list), 200

@city_bp.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = City.persistence.get(city_id, 'City')
    if city:
        return jsonify(city.to_dict()), 200
    return jsonify({'error': 'City not found'}), 404

@city_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    city = City.persistence.get(city_id, 'City')
    if city:
        city.name = data.get('name', city.name)
        city.country_code = data.get('country_code', city.country_code)
        city.save()
        return jsonify(city.to_dict()), 200
    return jsonify({'error': 'City not found'}), 404

@city_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.persistence.get(city_id, 'City')
    if city:
        city.delete()
        return jsonify({'success': 'City deleted'}), 200
    return jsonify({'error': 'City not found'}), 404
