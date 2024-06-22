from flask import Blueprint, jsonify
from models.country import Country

country_bp = Blueprint('country_bp', __name__)

@country_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    return jsonify([country.to_dict() for country in countries]), 200

@country_bp.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = Country.query.get(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.to_dict()), 200
