# HBnB Evolution Project

## Description

This project is the first step in creating a web application similar to AirBnB. This part focuses on the backend setup, including developing a UML model, implementing backend functionality using Flask, creating data persistence using simple classes, and containerizing the API using Docker.

## Project Structure

```
holbertonschool_hbnb_sgc/
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── user.py
│   ├── place.py
│   ├── city.py
│   ├── country.py
│   ├── review.py
│   ├── amenity.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── place.py
│   ├── city.py
│   ├── country.py
│   ├── review.py
│   ├── amenity.py
├── persistence/
│   ├── __init__.py
│   ├── persistence.py
├── tests/
│   ├── __init__.py
│   ├── test_user.py
│   ├── test_place.py
│   ├── test_city.py
│   ├── test_country.py
│   ├── test_review.py
│   ├── test_amenity.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup

### Install Dependencies

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/holbertonschool_hbnb_sgc.git
    cd holbertonschool_hbnb_sgc
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

```bash
flask run
```

### Running the Docker Container

1. Build the Docker image:
    ```bash
    docker build -t hbnb-evolution .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 hbnb-evolution
    ```

## Testing

```bash
python -m unittest discover tests
```

