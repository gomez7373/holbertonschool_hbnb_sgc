from flask import Blueprint, request, jsonify
from models.review import Review

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review = Review(
        place_id=data.get('place_id'),
        user_id=data.get('user_id'),
        rating=data.get('rating'),
        comment=data.get('comment')
    )
    review.save()
    return jsonify(review.to_dict()), 201

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.persistence.data['Review'].values()
    reviews_list = [review.to_dict() for review in reviews]
    return jsonify(reviews_list), 200

@review_bp.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.persistence.get(review_id, 'Review')
    if review:
        return jsonify(review.to_dict()), 200
    return jsonify({'error': 'Review not found'}), 404

@review_bp.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = Review.persistence.get(review_id, 'Review')
    if review:
        review.place_id = data.get('place_id', review.place_id)
        review.user_id = data.get('user_id', review.user_id)
        review.rating = data.get('rating', review.rating)
        review.comment = data.get('comment', review.comment)
        review.save()
        return jsonify(review.to_dict()), 200
    return jsonify({'error': 'Review not found'}), 404

@review_bp.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.persistence.get(review_id, 'Review')
    if review:
        review.delete()
        return jsonify({'success': 'Review deleted'}), 200
    return jsonify({'error': 'Review not found'}), 404
