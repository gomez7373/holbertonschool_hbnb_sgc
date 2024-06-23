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
    amenities = Amenity.persistence.data['Amenity'].values()
    amenities_list = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenities_list), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.persistence.get(amenity_id, 'Amenity')
    if amenity:
        return jsonify(amenity.to_dict()), 200
    return jsonify({'error': 'Amenity not found'}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = Amenity.persistence.get(amenity_id, 'Amenity')
    if amenity:
        amenity.name = data.get('name', amenity.name)
        amenity.save()
        return jsonify(amenity.to_dict()), 200
    return jsonify({'error': 'Amenity not found'}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = Amenity.persistence.get(amenity_id, 'Amenity')
    if amenity:
        amenity.delete()
        return jsonify({'success': 'Amenity deleted'}), 200
    return jsonify({'error': 'Amenity not found'}), 404
