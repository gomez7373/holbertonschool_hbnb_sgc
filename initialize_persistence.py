# initialize_persistence.py

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.country import Country
from models.review import Review
from models.amenity import Amenity
from persistence.data_manager import DataManager


# Initialize the persistence attribute
data_manager_instance = DataManager.instance()
BaseModel.persistence = data_manager_instance
