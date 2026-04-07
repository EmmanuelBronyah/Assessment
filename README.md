# USER CRUD API

This is a Python Django API that provides endpoints for creating, updating, retrieving, and deleting users based on role criteria.

## Features

- Create a user  
- Retrieve users by role (`admin`, `vendor`, `customer`, or `all`)  
- Update user details  
- Delete a user  

## Requirements

- Python 3.10+  
- Django  
- Other dependencies listed in `requirements.txt`  

## Installation

### 1. Clone the project

```bash
git clone https://github.com/EmmanuelBronyah/Assessment.git
cd Assessment
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Load seed data

```bash
python manage.py loaddata users
```

### 7. Run the server

```bash
python manage.py runserver
```

## API Endpoints

### Get Users by Role

- GET /users?role=admin
- GET /users?role=vendor
- GET /users?role=customer
- GET /users?role=all
  
### Create User

- POST /users

```json
{
  "name": "Yaw",
  "role": "customer"
}
```

### Update User

- PATCH /users/<id>

```json
{
  "name": "New Name",
  "role": "vendor"
}
```

### Delete User

- DELETE /users/<id>