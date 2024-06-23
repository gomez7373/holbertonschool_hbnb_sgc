import json
import os

class DataManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.data = {'User': {}, 'Place': {}, 'City': {}, 'Country': {}, 'Review': {}, 'Amenity': {}}
            cls._instance.load_data()
        return cls._instance

    def save_data(self):
        for entity_type, entities in self.data.items():
            serialized_data = {k: v.to_dict() for k, v in entities.items()}
            filename = f'data/{entity_type.lower()}.json'
            with open(filename, 'w') as f:
                json.dump(serialized_data, f)
            print(f"Saved data for {entity_type} to {filename}")

    def load_data(self, directory='data'):
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
            'Amenity': Amenity,
        }

        for entity_type in self.data.keys():
            filename = f'{directory}/{entity_type.lower()}.json'
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    loaded_data = json.load(f)
                    for entity_id, entity_data in loaded_data.items():
                        self.data[entity_type][entity_id] = entity_classes[entity_type](**entity_data)
                print(f"Loaded data for {entity_type} from {filename}")

    def save(self, entity):
        entity_type = entity.__class__.__name__
        self.data[entity_type][entity.id] = entity
        self.save_data()

    def get(self, entity_id, entity_type):
        return self.data[entity_type].get(entity_id)

    def update(self, entity):
        entity_type = entity.__class__.__name__
        self.data[entity_type][entity.id] = entity
        self.save_data()

    def delete(self, entity_id, entity_type):
        if entity_id in self.data[entity_type]:
            del self.data[entity_type][entity_id]
            self.save_data()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
