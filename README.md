# Django User Management API

A RESTful API for managing users, built with Django and Django REST framework. This project provides endpoints to create, retrieve, update, and delete user records.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [License](#license)

## Features

- **User Registration**: Create new users.
- **User Management**: View, update, and delete user information.
- **Admin Interface**: Django admin interface for managing users and data.
- **API Documentation**: Django REST Framework’s browsable API for testing and exploring endpoints.

## Technologies

- **Django**: 5.1.2
- **Django REST Framework**: Used for building RESTful API endpoints.
- **SQLite**: Default database for quick setup and development (can be changed to PostgreSQL, MySQL, etc.).

## Getting Started

### Prerequisites

- **Python 3.10+**
- **pip** (Python package installer)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/RishabhShrival/myproject.git
   cd django-user-management-api
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate     # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (for accessing the admin panel):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   The application will now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### API Endpoints

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| GET    | `/api/users/`      | Retrieve all users             |
| POST   | `/api/users/`      | Create a new user              |
| GET    | `/api/users/<id>/` | Retrieve a specific user by ID |
| PUT    | `/api/users/<id>/` | Update a user’s information    |
| DELETE | `/api/users/<id>/` | Delete a user                  |

> Note: The `<id>` in the endpoint URL refers to the user's unique ID.

### Usage

1. **Testing the API with curl**:

   - **Get all users**:

     ```bash
     curl -X GET http://127.0.0.1:8000/api/users/
     ```

   - **Create a new user**:

     ```bash
     curl -X POST http://127.0.0.1:8000/api/users/ -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com", "password": "securepassword123"}'
     ```

   - **Get a user by ID**:
     ```bash
     curl -X GET http://127.0.0.1:8000/api/users/1/
     ```

2. **Using the Django Admin Interface**:
   Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials to manage users and view data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Acknowledgments

- Built using Django and Django REST framework.
- Inspired by RESTful API best practices.
