# Holberton School - HBNB

Welcome to the HBNB project, a web application for managing rental services similar to Airbnb. This project is developed as part of the Holberton School curriculum, focusing on building a full-stack web application with a comprehensive backend and API.

## Table of Contents

- [Holberton School - HBNB](#holberton-school---hbnb)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Models](#models)
  - [API Routes](#api-routes)
    - [User Routes](#user-routes)
    - [Place Routes](#place-routes)
    - [City Routes](#city-routes)
    - [Country Routes](#country-routes)
    - [Review Routes](#review-routes)
    - [Amenity Routes](#amenity-routes)
  - [Running Tests](#running-tests)
  - [License](#license)
  - [Author](#author)

## Installation

To get started with the HBNB project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone git@github.com:gomez7373/holbertonschool_hbnb_sgc.git
    cd holbertonschool_hbnb_sgc
    ```

2. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the Flask application, run the following command:

```sh
python3 api/app.py

## Project Structure
Here is the structure of the project with descriptions of each file and directory:

holbertonschool_hbnb_sgc/
├── api/
│   ├── app.py             # Main Flask application file
│   ├── user.py            # User API routes
│   ├── place.py           # Place API routes
│   ├── city.py            # City API routes
│   ├── country.py         # Country API routes
│   ├── review.py          # Review API routes
│   └── amenity.py         # Amenity API routes
├── models/
│   ├── __init__.py        # Initialization file for models
│   ├── base_model.py      # BaseModel class definition
│   ├── user.py            # User model class
│   ├── place.py           # Place model class
│   ├── city.py            # City model class
│   ├── country.py         # Country model class
│   ├── review.py          # Review model class
│   └── amenity.py         # Amenity model class
├── persistence/
│   └── data_manager.py    # DataManager class for data management
├── tests/
│   └── ...                # Test files for models and API routes
├── data/
│   └── ...                # JSON files for data persistence
├── requirements.txt       # Python packages required for the project
└── README.md              # Project documentation

# Project Structure and API Documentation

## Project Structure

**api/**: Contains all the API route files, each handling the CRUD operations for different models.
**models/**: Contains the model classes, including BaseModel and specific classes for User, Place, City, Country, Review, and Amenity.
**persistence/**: Contains the DataManager class responsible for saving and loading data from JSON files.
**tests/**: Contains the unit tests for models and API routes.
**data/**: Contains JSON files used for data persistence.
**requirements.txt**: Lists the Python packages required to run the project.
**README.md**: This file, containing the project documentation.

## Models

The models are defined in the `models` directory and include the following classes:

**BaseModel**: The base class for all models, includes common attributes and methods.
**User**: Represents a user with attributes `email`, `first_name`, and `last_name`.
**Place**: Represents a rental place with various attributes like `host_id`, `name`, `description`, etc.
**City**: Represents a city with `name` and `country_code`.
**Country**: Represents a country with `code` and `name`.
**Review**: Represents a review with `place_id`, `user_id`, `rating`, and `comment`.
**Amenity**: Represents an amenity with `name`.

All models inherit from `BaseModel` and utilize the `BaseModel.persistence` reference for data management.

## API Routes

The API routes are defined in the `api` directory and include the following blueprints:

### User Routes

**Create a user**: `POST /users`
**Get all users**: `GET /users`
**Get a specific user**: `GET /users/<user_id>`
**Update a user**: `PUT /users/<user_id>`
**Delete a user**: `DELETE /users/<user_id>`

### Place Routes

**Create a place**: `POST /places`
**Get all places**: `GET /places`
**Get a specific place**: `GET /places/<place_id>`
**Update a place**: `PUT /places/<place_id>`
**Delete a place**: `DELETE /places/<place_id>`

### City Routes

**Create a city**: `POST /cities`
**Get all cities**: `GET /cities`
**Get a specific city**: `GET /cities/<city_id>`
**Update a city**: `PUT /cities/<city_id>`
**Delete a city**: `DELETE /cities/<city_id>`

### Country Routes

**Create a country**: `POST /countries`
**Get all countries**: `GET /countries`
**Get a specific country**: `GET /countries/<country_id>`
**Update a country**: `PUT /countries/<country_id>`
**Delete a country**: `DELETE /countries/<country_id>`

### Review Routes

**Create a review**: `POST /reviews`
**Get all reviews**: `GET /reviews`
**Get a specific review**: `GET /reviews/<review_id>`
**Update a review**: `PUT /reviews/<review_id>`
**Delete a review**: `DELETE /reviews/<review_id>`

### Amenity Routes

**Create an amenity**: `POST /amenities`
**Get all amenities**: `GET /amenities`
**Get a specific amenity**: `GET /amenities/<amenity_id>`
**Update an amenity**: `PUT /amenities/<amenity_id>`
**Delete an amenity**: `DELETE /amenities/<amenity_id>`

## Running Tests

To ensure the functionality of the models and API routes, run the tests using the `unittest` framework:

```sh
python3 -m unittest discover -s tests

