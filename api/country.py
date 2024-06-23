from flask import Blueprint, request, jsonify
from models.country import Country

country_bp = Blueprint('country_bp', __name__)

@country_bp.route('/countries', methods=['POST'])
def create_country():
    data = request.get_json()
    country = Country(code=data.get('code'), name=data.get('name'))
    country.save()
    return jsonify(country.to_dict()), 201

@country_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.persistence.data['Country'].values()
    countries_list = [country.to_dict() for country in countries]
    return jsonify(countries_list), 200

@country_bp.route('/countries/<country_id>', methods=['GET'])
def get_country(country_id):
    country = Country.persistence.get(country_id, 'Country')
    if country:
        return jsonify(country.to_dict()), 200
    return jsonify({'error': 'Country not found'}), 404

@country_bp.route('/countries/<country_id>', methods=['PUT'])
def update_country(country_id):
    data = request.get_json()
    country = Country.persistence.get(country_id, 'Country')
    if country:
        country.code = data.get('code', country.code)
        country.name = data.get('name', country.name)
        country.save()
        return jsonify(country.to_dict()), 200
    return jsonify({'error': 'Country not found'}), 404

@country_bp.route('/countries/<country_id>', methods=['DELETE'])
def delete_country(country_id):
    country = Country.persistence.get(country_id, 'Country')
    if country:
        country.delete()
        return jsonify({'success': 'Country deleted'}), 200
    return jsonify({'error': 'Country not found'}), 404
