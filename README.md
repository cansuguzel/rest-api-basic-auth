# REST API with Basic Authentication

This project provides two separate REST APIs developed with Python (Flask) and PostgreSQL. The APIs are protected with Basic Authentication.

# Project Structure
rest-api-basic-auth/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── auth.py
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
### Create a virtual environment

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
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/not_sistemi
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

#  Postman Testing
You can test all endpoints using Postman.
Go to Postman and set the Base URL:
   http://127.0.0.1:5000/api/v1/

All endpoints require Basic Auth:
- Use the Authorization tab in Postman
- Select Basic Auth
- Provide your registered username and password

# User API Endpoints
`POST /api/v1/users/`
Add a new user.
 Requires authentication (you can remove this if you want open registration).
Request: POST /api/v1/users/
Body: raw->json
{
  "username": "cansu",
  "password": "123456"
}
Response:
{
  "message": "Kayıt başarılı!"
}

`GET /api/v1/users/` 
Get all registered users.
Request: GET /api/v1/users/
Response:
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

`GET /api/v1/users/<user_id>`
Get details of a specific user by ID.
Request: GET /api/v1/users/1
Response:
{
  "id": 1,
  "username": "cansu"
}

`PUT /api/v1/users/<user_id> `
Update your own user information.

⚠️ Only the logged-in user can update their own data.
Request: PUT /api/v1/users/1
Body:
{
  "username": "cansu_updated",
  "password": "newpass123"
}
Response:
{
  "message": "Kullanıcı güncellendi.",
  "user": {
    "id": 1,
    "username": "cansu_updated"
  }
}

 `DELETE /api/v1/users/<user_id>`
Delete your own user account.
⚠️ Only the user themselves can delete their account.
Request: DELETE /api/v1/users/1
Response:
Status code: 204 No Content

# Notes API Endpoints
`GET /api/v1/notes `
Get all notes for the current user.
Request: GET /api/v1/notes
Response:
[
  {
    "id": 1,
    "title": "Shopping List",
    "content": "Milk, Bread, Eggs"
  }
]

`POST /api/v1/notes`
Add a new note.
Request: POST /api/v1/notes
Body:
{
  "title": "Todo",
  "content": "Finish the project"
}
Response:
{
  "message": "Not eklendi.",
  "note_id": 2
}

`GET /api/v1/notes/<note_id>`
Get a specific note by ID.
Request: GET /api/v1/notes/1
Response:
{
  "id": 1,
  "title": "Shopping List",
  "content": "Milk, Bread, Eggs"
}

`PUT /api/v1/notes/<note_id>`
Update a note.
Request: PUT /api/v1/notes/1
Body:
{
  "title": "Updated List",
  "content": "Milk, Bread, Eggs, Cheese"
}
Response:
{
  "message": "Not güncellendi.",
  "note": {
    "id": 1,
    "title": "Updated List",
    "content": "Milk, Bread, Eggs, Cheese"
  }
}

`DELETE /api/v1/notes/<note_id>`
Delete a note.

Request: DELETE /api/v1/notes/1
Response:
Status: 204 No Content

### Postman Collection
A Postman collection file is included in this project for easy API testing.
File:
  Rest API Basic Auth.postman_collection.json
This file contains sample requests for all endpoints, including proper authentication and body examples.
* How to Use:
 - Open Postman
 - Go to File → Import
 - Select the Rest API Basic Auth.postman_collection.json file from this project
 - Test the API endpoints easily with pre-filled data

### Database Info
Database: PostgreSQL
DB Name: not_sistemi
Tables: user, note
ORM: SQLAlchemy


### Developer
 Name: Cansu Güzel
 Project: RESTful API with Basic Authentication