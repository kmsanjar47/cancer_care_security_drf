# Django REST Framework API with JWT Authentication and Swagger Documentation

This is a Django-based API project that implements JWT authentication, user registration, role-based access control, PostgreSQL integration, and provides interactive API documentation with Swagger.

## Features
- JWT Authentication (Login/Logout)
- User Registration
- Role-based access (Admin/User)
- PostgreSQL database
- Swagger for API documentation

## Requirements
- Python 3.x
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

```
### 2. Create a Virtual Environment

Next, create a virtual environment to isolate your dependencies:

```
python -m venv venv

```

### Activate your virtual environment

```
venv\Scripts\activate

```
### 3. Install Dependencies

With the virtual environment activated, install the required packages from requirements.txt:

```
pip install -r requirements.txt

```
### 4. Configure Database Settings

This project uses PostgreSQL as the database. You need to update your database credentials in the settings.py file.

Open settings.py and locate the DATABASES section:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # or your database server IP
        'PORT': '5432',       # Default port for PostgreSQL
    }
}

```
Replace your_db_name, your_db_user, and your_db_password with your actual PostgreSQL credentials.

### 5. Apply Migrations
After configuring your database, run the following commands to apply migrations and set up the database:

```
python manage.py migrate

```
### 6. Run the Development Server
Now you can run the Django development server:

```
python manage.py runserver

```
The API will be available at http://127.0.0.1:8000/

### 7. Access Swagger API Documentation
Swagger documentation is automatically generated for your API. You can access it by navigating to:

```
http://127.0.0.1:8000/swagger/

```
This will open an interactive Swagger UI, where you can explore and test the API endpoints.
