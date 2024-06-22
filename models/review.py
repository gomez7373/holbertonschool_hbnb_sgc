from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, place_id, user_id, rating, comment, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        review_dict = super().to_dict()
        review_dict.update({
            'place_id': self.place_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment
        })
        return review_dict
