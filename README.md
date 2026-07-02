EventHub
EventHub is a backend API for a simplified event ticketing platform. Users can browse events, reserve seats, cancel reservations, and filter data using query parameters.

The project is built using Django, Django REST Framework, Django ORM models, serializers, ViewSets, routers, and custom middleware.

Features
Create, list, retrieve, update, and delete events

Create, list, retrieve, update, and delete reservations

Filter events by status

Filter events by venue

Filter reservations by event ID

Reserve seats for an event

Automatically deduct available seats when a reservation is created

Cancel a reservation

Automatically restore seats when a reservation is cancelled

Prevent overbooking

Log every request using custom middleware

Tech Stack
Python

Django

Django REST Framework

SQLite

Postman

Project Structure
eventhub/
├── manage.py
├── eventhub/
│   ├── settings.py
│   └── urls.py
├── events/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── middleware.py
│   └── migrations/
├── requirements.txt
└── README.md
How to Run the Project
Clone the repository:

git clone <your-github-repo-url>
cd eventhub
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Run migrations:

python manage.py migrate
Start the server:

python manage.py runserver
The API will run at:

http://127.0.0.1:8000/
API Endpoints
Event Endpoints
Method	Endpoint	Description
GET	/api/events/	List all events
POST	/api/events/	Create a new event
GET	/api/events/{id}/	Get a single event
PUT	/api/events/{id}/	Replace an event
PATCH	/api/events/{id}/	Partially update an event
DELETE	/api/events/{id}/	Delete an event
GET	/api/events/?status=upcoming	Filter events by status
GET	/api/events/?venue=Bangalore	Filter events by venue
Reservation Endpoints
Method	Endpoint	Description
GET	/api/reservations/	List all reservations
POST	/api/reservations/	Create a reservation
GET	/api/reservations/{id}/	Get a single reservation
PUT	/api/reservations/{id}/	Replace a reservation
PATCH	/api/reservations/{id}/	Partially update a reservation
DELETE	/api/reservations/{id}/	Delete a reservation
GET	/api/reservations/?event_id=1	Filter reservations by event ID
POST	/api/reservations/{id}/cancel/	Cancel a reservation
Sample Create Event Request
{
  "title": "PyCon India 2025",
  "venue": "NIMHANS Convention Centre, Bangalore",
  "date": "2025-09-20",
  "total_seats": 500,
  "available_seats": 500,
  "status": "upcoming"
}
Sample Create Reservation Request
{
  "event": 1,
  "attendee_name": "Priya Sharma",
  "attendee_email": "priya@example.com",
  "seats_reserved": 2
}
Sample Successful Reservation Response
{
  "id": 1,
  "event": 1,
  "attendee_name": "Priya Sharma",
  "attendee_email": "priya@example.com",
  "seats_reserved": 2,
  "status": "confirmed",
  "created_at": "2026-06-24T10:00:00Z"
}
Sample Overbooking Failure Response
{
  "non_field_errors": [
    "Only 1 seat(s) available."
  ]
}
Sample Cancellation Endpoint
POST /api/reservations/1/cancel/
No request body is needed.

Design Decision
I handled seat deduction inside the create() method of ReservationSerializer. This keeps reservation creation and seat update logic in one place. When a reservation is created, the event's available_seats value is reduced before the reservation object is saved.

For cancellation, I used a custom ViewSet action called cancel. This allows a clean endpoint like /api/reservations/{id}/cancel/, which clearly represents the action being performed.

In a production ticketing system with many users booking at the same time, I would use transaction.atomic() and row-level locking to prevent race conditions. For this assignment, keeping the logic inside the serializer and ViewSet is simple and matches the required implementation.