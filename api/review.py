from flask import Blueprint, request, jsonify
from models.review import Review

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.get_json()
    review = Review(place_id=place_id, user_id=data.get('user_id'), rating=data.get('rating'), comment=data.get('comment'))
    review.save()
    return jsonify(review.to_dict()), 201

@review_bp.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    reviews = Review.query.filter_by(place_id=place_id).all()
    return jsonify([review.to_dict() for review in reviews]), 200

@review_bp.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.to_dict()), 200

@review_bp.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)
    review.save()
    return jsonify(review.to_dict()), 200

@review_bp.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    review.delete()
    return '', 204
