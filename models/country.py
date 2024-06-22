from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, code, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = code
        self.name = name

    def to_dict(self):
        country_dict = super().to_dict()
        country_dict.update({
            'code': self.code,
            'name': self.name
        })
        return country_dict
