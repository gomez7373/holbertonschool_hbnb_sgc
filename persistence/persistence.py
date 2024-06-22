from abc import ABC, abstractmethod

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
