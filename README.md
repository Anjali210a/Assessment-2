# Assessment-2

🔧 What This Project Does:
It lets you:

📥 Add a contact

🧾 View all contacts

✏️ Edit a contact

❌ Delete a contact

🔄 See updates in real-time if someone else makes a change

🧱 How Everything Works Together (In Simple Words):
1. Django (Main Backend)
Django is the brain of your app. It handles:

The website logic

Talks to the database

Sends and receives data through APIs

2. MongoDB (Database)
MongoDB is where all the contact info (like name, phone, email) is stored.

It's a NoSQL database (stores data in a flexible format like JSON)

Django uses djongo to talk to MongoDB

3. REST API (Django REST Framework)
The REST API is like a menu. It lets users:

GET: read contact info

POST: add a contact

PUT/PATCH: update contact info

DELETE: remove a contact

Users (or frontend apps like React, Postman, etc.) send requests to these APIs.

4. WebSocket + Django Channels + Redis
This part gives real-time updates.

A WebSocket is like an open call between the user and the server.

Django Channels handles that WebSocket connection.

Redis helps Django send the same update to all connected users.

So when you add/edit/delete a contact, all users see that change instantly.

🔄 Example: What Happens When You Add a Contact
You send a request like:
"Add a contact: Anjali, 9999999999, anjali@mail.com"
using the API.

Django receives it, saves it to MongoDB.

Django tells Redis:
"Hey! A new contact was added!"

Redis tells all users connected via WebSocket:
"New contact alert! Update your contact list!"





| Component            | Role                               |
| -------------------- | ---------------------------------- |
| **Django**           | Handles the backend logic          |
| **MongoDB**          | Stores contact data                |
| **Django REST**      | Provides API endpoints (CRUD)      |
| **Channels + Redis** | Pushes real-time updates           |
| **WebSocket**        | Keeps the browser always listening |




# Contact Management System

A Django-based Contact Management System that allows users to add, update, and delete contact entries with real-time updates. Built with MongoDB as the backend database and Django Channels + Redis for WebSocket-based live updates.

## Features
- Add, Edit, Delete Contacts
- MongoDB for document-based storage
- Django Admin Panel for management
- REST API using Django REST Framework
- Real-time updates using Django Channels and Redis

## Tech Stack
- **Backend:** Django
- **Database:** MongoDB (via Djongo)
- **Real-Time:** Django Channels, Redis
- **API:** Django REST Framework

## Getting Started

### Prerequisites
- Python 3.8+
- MongoDB
- Redis

### Installation
```bash
git clone https://github.com/yourusername/contact-management-system.git
cd contact-management-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in your root project directory:
```
MONGO_DB_NAME=your_db
MONGO_USER=your_user
MONGO_PASS=your_pass
MONGO_HOST=localhost
MONGO_PORT=27017
```
Make sure to load these in `settings.py` using `os.environ.get()`.

### Running the Project
```bash
sudo systemctl start mongod
sudo systemctl start redis
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:
- Admin Panel: http://127.0.0.1:8000/admin/
- API Endpoint: http://127.0.0.1:8000/api/contacts/
- WebSocket: ws://127.0.0.1:8000/ws/contacts/

### Deployment
Add a `Procfile` if deploying on Heroku:
```
web: daphne contact_project.asgi:application
```


**.gitignore**
venv/
__pycache__/
*.pyc
.env
db.sqlite3


**Procfile**
web: daphne contact_project.asgi:application
