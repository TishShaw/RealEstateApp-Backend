# Realty Homes Django Backend

This backend, built with Django and Django Rest Framework, leverages PostgreSQL for database management and the simple-jwt package for secure user authentication. It's designed to efficiently handle real estate data and user interactions within the Realty Homes application.
 
## Table of Contents
- [Project Overview](#project-overview)
- [Installation and Setup](#installation-and-setup)
- [API Endpoints and Usage](#api-endpoints)
- [Authentication and Security](#authentication-and-security)
- [Database Configuration](#database-configuration)
- [Contributions](#contributions)

## Installation and Setup

### Step 1: Setting Up a Virtual Environment
It is recommended to use a virtual environment for Django projects to manage dependencies effectively.

1. ***Create a Virtual Environment***: 
`python -m venv myenv` <br>
myenv is the name of the virtual environment. You can name it anything you prefer.

2. ***Activate the Virtual Environment***:

- On Windows:
`
myenv\Scripts\activate
`
- On macOS and Linux:
`
source myenv/bin/activate
`
### Step 2: Installing Django
With the virtual environment activated, install Django using pip, Python's package manager. <br>
`
pip install django
`
### Step 3: Creating a Django Project
Create a new Django project by running: <br>
`
django-admin startproject myproject
`
<br>
<br>
Replace myproject with your desired project name.

### Step 4: Installing Django REST Framework
Django REST Framework is an essential tool for building RESTful APIs with Django. Install it using pip: <br>

`
pip install djangorestframework
`
### Step 5: Configuring Django REST Framework in Your Project
To use Django REST Framework, you need to add it to the installed apps in your Django settings.

Navigate to your project's settings.py file.

In the INSTALLED_APPS section, add 'rest_framework'.

```
INSTALLED_APPS = [
    # ... existing apps ...
    'rest_framework',
]
```

### Step 6: Running the Django Server
To verify that everything is set up correctly, you can run the Django development server.

`
python manage.py runserver
`
<br>
<br>

If everything is set up correctly, you should see a message indicating that the server is running. You can then navigate to **http://127.0.0.1:8000/** in your web browser to see the Django welcome page.

## API Endpoints
The Django backend exposes several RESTful API endpoints for interacting with the application. Below is a list of available endpoints along with their methods and functionality.


### User Management
- Create a new user account
  - POST:  /register/
- Retrieve details of the current authenticated user
  - GET: /api/user/
- Obtain a JWT for authenticated access.
  - POST: /api/token/
- Refresh the JWT token
  - POST: /api/token/refresh/
- Add a property to the user's favorites
  - POST: api/user/add-favorite/<int:property_id>/
- Remove a property from the user's favorites
  - POST: api/user/remove-favorite/<int:property_id>/ 

### Property Management
- Retrieve a list of all properties available.
  - GET: /properties/
 
## Authentication and Securtiy
In this project, I used **simple-jwt** library to handle JSON Web Token(JWT). This framework enhances the security of our backend by ensuring that only authenticated users can access specific API endpoints.

### Implementation of JWT in Django
- ***Token Generation***: Upon successful authentication, the system generates a JWT for the user. This token serves as a secure credential for accessing protected endpoints in the application.
- ***Token Validation***: Each request to a secured endpoint must include the JWT in the Authorization header. The backend validates this token before granting access to the requested resources.
- ***Secure Transmission***: Tokens are only transmitted over HTTPS, ensuring that user credentials are encrypted and protected during transit.

## Database Configuration

### PostgreSQL Setup
This project uses PostgreSQL as its primary database to store user data and property data.
### Initial Configuration
1. **Install PostgreSQL**: Ensure PostgreSQL is installed on your machine. Installation guides can be found on the official PostgreSQL website.
2. **Create Database**: Create a new PostgreSQL database for the project. I used pgAdmin GUI to create the database but you can also do this through the command line.
  `CREATE DATABASE realty_homes_db;`
3. **User and Permissions**: Create a user and grant necessary permissions to the database.
   `CREATE USER myuser WITH PASSWORD 'mypassword';`
`GRANT ALL PRIVILEGES ON DATABASE realty_homes_db TO myuser;
`

### Django Database Settings
In your Django project's settings file (usually settings.py), configure the DATABASES setting to use PostgreSQL:
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'realty_homes_db',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',  # Set to your database host
        'PORT': '',  # Leave blank to use the default port
    }
}
```

### Migrations
Once the database is set up and configured, run Django migrations to create the necessary tables:
`python manage.py migrate`

## Contributions
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a pull request with a fix, reference the issue you created.
