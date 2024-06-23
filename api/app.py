import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from flask import Flask
import initialize_persistence  # Ensure persistence is initialized
from api.user import user_bp
from api.place import place_bp
from api.city import city_bp
from api.country import country_bp
from api.review import review_bp
from api.amenity import amenity_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(place_bp)
app.register_blueprint(city_bp)
app.register_blueprint(country_bp)
app.register_blueprint(review_bp)
app.register_blueprint(amenity_bp)

@app.route('/')
def index():
    return "Welcome to HBnB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
