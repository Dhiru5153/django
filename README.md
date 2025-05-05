# Django User Management App

This is a simple Django web application for managing users with roles such as "admin" and "user".

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Dhiru5153/django.git
cd user_project

### 2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate 
#On Windows use: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

###  4. Configure MySQL Database

## Update the DATABASES section in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

##  Make sure the database exists:
CREATE DATABASE users_db;

###  5. Apply Migrations

python manage.py makemigrations
python manage.py migrate

###  6. Create a Superuser (Optional)

python manage.py createsuperuser

###  7. Run the Server

python manage.py runserver
#Visit http://127.0.0.1:8000 to use the application.

###  Requirements

## Dependencies are listed in requirements.txt. To install:
pip install -r requirements.txt

