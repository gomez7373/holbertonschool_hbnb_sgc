import uuid
from datetime import datetime
from persistence.persistence import DataManager

class BaseModel:
    persistence = DataManager()

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        BaseModel.persistence.save(self)

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def delete(self):
        BaseModel.persistence.delete(self.id, self.__class__.__name__)
