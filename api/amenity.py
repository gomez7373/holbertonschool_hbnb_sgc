from flask import Blueprint, request, jsonify
from models.amenity import Amenity

amenity_bp = Blueprint('amenity_bp', __name__)

@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    amenity = Amenity(name=data.get('name'))
    amenity.save()
    return jsonify(amenity.to_dict()), 201

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = Amenity.query.all()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.to_dict()), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    amenity.name = data.get('name', amenity.name)
    amenity.save()
    return jsonify(amenity.to_dict()), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    amenity.delete()
    return '', 204
