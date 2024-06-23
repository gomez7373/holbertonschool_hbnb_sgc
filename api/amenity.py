from flask import Blueprint, request, jsonify
from models.amenity import Amenity
from persistence.persistence import DataManager

amenity_bp = Blueprint('amenity_bp', __name__)
data_manager = DataManager()

@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    amenity = Amenity(name=data.get('name'))
    data_manager.save(amenity)
    return jsonify(amenity.to_dict()), 201

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = data_manager.data['Amenity'].values()
    amenities_list = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenities_list), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    amenity.name = data.get('name', amenity.name)
    data_manager.update(amenity)
    return jsonify(amenity.to_dict()), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = data_manager.get(amenity_id, 'Amenity')
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    data_manager.delete(amenity_id, 'Amenity')
    return '', 204
