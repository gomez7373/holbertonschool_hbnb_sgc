from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_code, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.country_code = country_code

    def to_dict(self):
        city_dict = super().to_dict()
        city_dict.update({
            'name': self.name,
            'country_code': self.country_code
        })
        return city_dict
