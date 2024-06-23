import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        from persistence.data_manager import DataManager
        DataManager.instance().save(self)

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def delete(self):
        from persistence.data_manager import DataManager
        DataManager.instance().delete(self.id, self.__class__.__name__)
