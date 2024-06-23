import json
import os
from abc import ABC, abstractmethod
from models.user import User
from models.place import Place
from models.city import City
from models.country import Country
from models.review import Review
from models.amenity import Amenity

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        pass

class DataManager(IPersistenceManager):
    _instance = None

    def __init__(self, storage_path='data'):
        self.data = {'User': {}, 'Place': {}, 'City': {}, 'Country': {}, 'Review': {}, 'Amenity': {}}
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    @staticmethod
    def instance():
        if DataManager._instance is None:
            DataManager._instance = DataManager()
        return DataManager._instance

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

    def save_data(self):
        for entity_type, entities in self.data.items():
            file_path = os.path.join(self.storage_path, f"{entity_type.lower()}.json")
            with open(file_path, 'w') as f:
                json.dump({entity_id: entity.to_dict() for entity_id, entity in entities.items()}, f)
            print(f"Saved data for {entity_type} to {file_path}")

    def load_data(self):
        for entity_type in self.data.keys():
            file_path = os.path.join(self.storage_path, f"{entity_type.lower()}.json")
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    entities = json.load(f)
                    for entity_id, entity_data in entities.items():
                        entity_class = globals()[entity_type]
                        self.data[entity_type][entity_id] = entity_class(**entity_data)
                print(f"Loaded data for {entity_type} from {file_path}")
