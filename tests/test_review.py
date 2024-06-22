import unittest
from models.review import Review
from uuid import uuid4

class TestReview(unittest.TestCase):
    def test_review_creation(self):
        review = Review(place_id=str(uuid4()), user_id=str(uuid4()), rating=5, comment="Amazing place!")
        self.assertIsNotNone(review.id)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Amazing place!")

    def test_review_to_dict(self):
        review = Review(place_id=str(uuid4()), user_id=str(uuid4()), rating=5, comment="Amazing place!")
        review_dict = review.to_dict()
        self.assertEqual(review_dict['rating'], 5)
        self.assertEqual(review_dict['comment'], "Amazing place!")
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

if __name__ == '__main__':
    unittest.main()
