# Event Management System

This is a **Django-based Event Management System** that allows users to create and manage events, register for events, and filter them by category. Users can create an account, log in, and participate in the event registration process. The system supports user authentication, category-based filtering, and a responsive event list.

## Features

- **User Registration and Login:** Allows users to create an account, log in, and access protected features like event registration.
- **Event Creation:** Authenticated users can create new events, specifying details such as title, description, location, and category.
- **Event Registration:** Users can register for events, and their registration data is stored.
- **Category Filtering:** Events are organized into categories, making it easy for users to filter events by category.
- **Search Functionality:** Users can search for events by title.
- **Admin Dashboard:** Admins can manage events, registrations, and categories through Django's admin interface.

## Technologies Used

- **Django 5.0.7**: Web framework for backend logic and routing.
- **SQLite**: Default database for storing event, category, and user data.
- **HTML/CSS**: Frontend for rendering pages.
- **Django Admin**: For managing event data and user registrations.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Django 5.x installed via pip.

To install Django, use the following command:
```bash
pip install django
```

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/event-management-system.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd event-management-system
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Go to `http://127.0.0.1:8000/` in your browser to view the app.
   - Go to `http://127.0.0.1:8000/admin/` to access the admin dashboard.

### Project Structure

```text
event_management/
├── event_management/  # Main project settings
│   ├── settings.py
│   └── urls.py
├── events/            # Main app containing event logic
│   ├── models.py      # Event, Category, Registration models
│   ├── views.py       # View functions for handling requests
│   ├── forms.py       # Django forms for event creation/registration
│   └── templates/     # HTML templates for rendering views
│       ├── home.html
│       ├── event_list.html
│       └── ...
├── db.sqlite3         # SQLite database
└── manage.py          # Django management commands
```

## Usage

- **Create Events**: After logging in, users can create events and select a category.
- **Register for Events**: Users can browse events and register for them.
- **Filter by Category**: Events can be filtered by their associated categories.

## Admin Access

The Django admin panel allows administrators to manage events, categories, and user registrations. Once you've created a superuser, you can log in at `/admin` to manage the database.

## Future Enhancements

- Add a user profile page for managing event registrations.
- Integrate email notifications for event reminders.
- Add pagination for event lists.

