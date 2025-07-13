# REST API with Basic Authentication

This project implements two separate RESTful APIs — one for user management and another for note management — built with Python (Flask) and PostgreSQL. All endpoints are secured using Basic Authentication.User passwords are securely hashed using Werkzeug before storing in the database.Access control and user authorization are managed via custom decorators (@basic_auth_required, @self_access_required, @owner_required) to enforce security consistently across endpoints.

# Project Structure
rest-api-basic-auth/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── auth.py
│ ├──decorators.py
│ ├── routes/
│ │ ├── init.py
│ │ ├── users.py
│ │ └── notes.py
│
├── create_db.py
├── run.py
├── config.py
├── requirements.txt
└── README.md
 
# Clone the repository

```bash
git clone https://github.com/cansuguzel/rest-api-basic-auth.git
cd rest-api-basic-auth
``` 
# Create a virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate
``` 
# Install dependencies

```bash
pip install -r requirements.txt
``` 
# Configure environment (optional)

If you're using .env for DB connection:
```bash
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/database_name
```
(If you're directly editing config in code, this step is not required.)

# Initialize the database

Make sure PostgreSQL is running, then run:
```bash
python create_db.py
```
# Run the server
```bash
python run.py
```
API will run on: http://127.0.0.1:5000

## Authentication
All endpoints require Basic Auth:

- Use the Authorization tab in Postman
- Select Basic Auth
- Provide your registered username and password

You can test all endpoints using Postman.

Go to Postman and set the Base URL:
   http://127.0.0.1:5000/api/v1/

# User API Endpoints
`POST /api/v1/users/`
Add a new user.
Request: POST /api/v1/users/

**Body: raw->json**
 ```json
{
  "username": "cansu",
  "password": "123456"
}
```
Response:
 ```json
{
  "message": "Registration successful!"
}
```
`POST /api/v1/users/login`
This endpoint is only a test endpoint to verify your credentials
Request: POST /api/v1/users/login
 ```json
{
  "username": "cansu",
  "password": "123456"
}
```
Response:
 ```json
{
   "message": "Login successful, welcome cansu!"
}
```

`GET /api/v1/users/` 
List all users (only if logged in).
Request: GET /api/v1/users/
Response:
 ```json
[
  {
    "id": 1,
    "username": "cansu"
  },
  {
    "id": 2,
    "username": "admin"
  }
]
 ```

`GET /api/v1/users/<user_id>`
Get details of a specific user by ID.
Request: GET /api/v1/users/1
Response:
 ```json
{
  "id": 1,
  "username": "cansu"
}
 ```
`PUT /api/v1/users/<user_id> `
Update your own account.

Request: PUT /api/v1/users/1
Body:
 ```json
{
  "username": "cansu_updated",
  "password": "newpass123"
}
 ```
Response:
 ```json
{
  "message": "User updated.",
  "user": {
    "id": 1,
    "username": "cansu_updated"
  }
}
 ```
 `DELETE /api/v1/users/<user_id>`
Delete your own user account.

Request: DELETE /api/v1/users/1
Response:
Status code: 204 No Content

# Notes API Endpoints
`GET /api/v1/notes `
Get all notes for the current user.
Request: GET /api/v1/notes
Response:
 ```json
[
  {
    "id": 1,
    "title": "Shopping List",
    "content": "Milk, Bread, Eggs"
  }
]
 ```
`POST /api/v1/notes`
Add a new note.
Request: POST /api/v1/notes
Body:
 ```json
{
  "title": "Todo",
  "content": "Finish the project"
}
 ```
Response:
 ```json
{
  "message": "Note added.",
  "note_id": 2
}
 ```
`GET /api/v1/notes/<note_id>`
Get a specific note you own.
Request: GET /api/v1/notes/1
Response:
 ```json
{
  "id": 1,
  "title": "Shopping List",
  "content": "Milk, Bread, Eggs"
}
 ```
`PUT /api/v1/notes/<note_id>`
Update your own note.
Request: PUT /api/v1/notes/1
Body:
 ```json
{
  "title": "Updated List",
  "content": "Milk, Bread, Eggs, Cheese"
}
 ```
Response:
 ```json
{
  "message": "Note updated.",
  "note": {
    "id": 1,
    "title": "Updated List",
    "content": "Milk, Bread, Eggs, Cheese"
  }
}
 ```

`DELETE /api/v1/notes/<note_id>`
Delete your own note.

Request: DELETE /api/v1/notes/1
Response:
Status: 204 No Content

### Postman Collection
A Postman collection file is included in this project for easy API testing.
File:
  Rest API Basic Auth.postman_collection2.json
This file contains sample requests for all endpoints, including proper authentication and body examples.
How to Use:
 - Open Postman
 - Go to File → Import
 - Select the Rest API Basic Auth.postman_collection2.json file from this project
 - Test the API endpoints easily with pre-filled data

### Database Info
Database: PostgreSQL

DB Name: not_sistemi

Tables: user, note

ORM: SQLAlchemy

## Technologies Used
- Python 
- Flask
- SQLAlchemy
- PostgreSQL
- Basic Authantication
- Secure password hashing (`werkzeug.security`)
- Postman (for test)

### Developer
 Name: Cansu Güzel

 Project: RESTful API with Basic Authentication