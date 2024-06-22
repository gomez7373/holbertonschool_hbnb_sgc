from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, email, first_name, last_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return user_dict
