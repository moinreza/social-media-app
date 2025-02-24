# Social Media App

A simple social media application built with Django that allows users to register, log in, create posts, and interact with others.

## Features
- User authentication (Sign up, Login, Logout)
- Create, edit, and delete posts
- View a global feed of posts
- User profiles with post history
- Secure authentication and session management

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.9+
- Django 5.x
- Git
- SQLite3 (or another database if configured)
- Virtual environment (recommended)

### Clone the Repository
```sh
git clone https://github.com/moinreza/social-media-app.git
cd social-media-app
```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Apply Migrations
```sh
python manage.py migrate
```

### Create a Superuser (Optional, for Admin Access)
```sh
python manage.py createsuperuser
```

### Run the Development Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## Database Schema & ERD
To generate an Entity-Relationship Diagram (ERD), ensure you have `django-extensions` installed:
```sh
pip install django-extensions
python manage.py graph_models -a -o erd.png
```

## Deployment
To deploy the application on a production server:
- Use **Gunicorn** and **NGINX**
- Configure **PostgreSQL** or **MySQL** instead of SQLite
- Use **Docker** and **CI/CD pipelines** for efficient deployment

## Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m "Description of changes"`
4. Push to your branch: `git push origin feature-branch`
5. Open a Pull Request

## License
This project is open-source and available under the MIT License.
