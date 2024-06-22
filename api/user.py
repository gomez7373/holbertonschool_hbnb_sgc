from flask import Blueprint, request, jsonify
from models.user import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(email=data.get('email'), first_name=data.get('first_name'), last_name=data.get('last_name'))
    user.save()
    return jsonify(user.to_dict()), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.persistence.data['User'].values()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list), 200

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.persistence.get(user_id, 'User')
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.persistence.get(user_id, 'User')
    if user:
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.save()
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.persistence.get(user_id, 'User')
    if user:
        user.delete()
        return jsonify({'success': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404
