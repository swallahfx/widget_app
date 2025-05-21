# Widget REST API

A simple CRUD REST API for managing Widget resources, built with Django and Django REST Framework.

## Features

- Full CRUD operations for Widget resources
- SQLite database for persistence
- OpenAPI specification (via Swagger and ReDoc)
- Type annotations
- Pytest for testing
- PEP8 compliance
- Security analysis with bandit

## Widget Properties

- `name`: UTF8 string limited to 64 characters
- `number_of_parts`: Integer
- `created_date`: Automatically set date/time
- `updated_date`: Automatically updated date/time

## Requirements

- Python 3.8 or later
- Django
- Django REST Framework
- Pytest

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```
   python manage.py migrate
   ```

## Running the Application

```
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/api/widgets/

## API Endpoints

- `GET /api/widgets/`: List all widgets
- `POST /api/widgets/`: Create a new widget
- `GET /api/widgets/{id}/`: Retrieve a specific widget
- `PUT /api/widgets/{id}/`: Update a specific widget
- `DELETE /api/widgets/{id}/`: Delete a specific widget

## API Documentation

- Swagger UI: http://127.0.0.1:8000/swagger/
- ReDoc: http://127.0.0.1:8000/redoc/

## Testing

### Running Tests

```
pytest
```

### Test Coverage

```
pytest --cov=widgets
```

### Test Structure

Tests are organized into:
- `conftest.py`: Common fixtures and setup for tests
- `route_test.py`: API endpoint tests
- `logic_test.py`: Model and business logic tests

## Running Linting

```
flake8
```

## Running Security Analysis

```
bandit -r .
```
