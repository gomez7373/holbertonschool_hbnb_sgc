# persistence/data_manager.py
import json

class DataManager:
    def __init__(self):
        self.data = {'User': {}, 'Place': {}, 'City': {}, 'Country': {}, 'Review': {}, 'Amenity': {}}

    def save(self, entity):
        entity_type = entity.__class__.__name__
        self.data[entity_type][entity.id] = entity

    def get(self, entity_id, entity_type):
        return self.data[entity_type].get(entity_id)

    def update(self, entity):
        entity_type = entity.__class__.__name__
        self.data[entity_type][entity.id] = entity

    def delete(self, entity_id, entity_type):
        if entity_id in self.data[entity_type]:
            del self.data[entity_type][entity_id]

    def save_data(self, filename):
        with open(filename, 'w') as f:
            json.dump({k: {ek: ev.to_dict() for ek, ev in v.items()} for k, v in self.data.items()}, f)

    def load_data(self, filename):
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.country import Country
        from models.review import Review
        from models.amenity import Amenity
        
        entity_classes = {
            'User': User,
            'Place': Place,
            'City': City,
            'Country': Country,
            'Review': Review,
            'Amenity': Amenity
        }
        
        with open(filename, 'r') as f:
            raw_data = json.load(f)
        
        for entity_type, entities in raw_data.items():
            entity_class = entity_classes[entity_type]
            for entity_id, entity_data in entities.items():
                entity = entity_class(**entity_data)
                self.data[entity_type][entity_id] = entity
