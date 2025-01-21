# Django Backend Project

A Python Django backend project integrating AWS services (RDS, EC2, S3) with an `onlineshop` app for order management.

## Features
- Django Framework for rapid development.
- `onlineshop` app with `/order` endpoint for CRUD operations.
- AWS RDS for database hosting.
- AWS EC2 for application hosting.
- AWS S3 for file storage.

## Prerequisites
- Python 3.8+
- `pip`
- Git
- PostgreSQL/MySQL client (if required locally)

## Setup Instructions
```bash
# Clone the repository
git clone https://github.com/Ajithpmdwaraka/django-backend.git
cd django-backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate    # Linux/MacOS
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Add environment variables
# Create a .env file in the project root with the following:
# SECRET_KEY=your_django_secret_key
# DEBUG=True
# AWS_ACCESS_KEY_ID=your_aws_access_key_id
# AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
# AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
# DATABASE_URL=your_database_url

# Apply database migrations
python manage.py migrate

# Start the server
python manage.py runserver
