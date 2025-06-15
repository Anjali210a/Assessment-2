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



contact_manager/
├── manage.py
├── contact_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py       # Needed for Channels
│   ├── wsgi.py
├── contacts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── consumers.py  # WebSocket handling
├── requirements.txt




| Component            | Role                               |
| -------------------- | ---------------------------------- |
| **Django**           | Handles the backend logic          |
| **MongoDB**          | Stores contact data                |
| **Django REST**      | Provides API endpoints (CRUD)      |
| **Channels + Redis** | Pushes real-time updates           |
| **WebSocket**        | Keeps the browser always listening |
