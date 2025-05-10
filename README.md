# E-Paan Store

E-Paan Store is a full-featured online paan ordering platform built with Django, MySQL, and HTML templates. Users can browse products, add items to their cart, place orders, and make payments — all through a clean and interactive interface.

---
## Tech Stack
**Frontend:**

    HTML (Django Templates)
    CSS
    JavaScript

**Backend:**

    Django
    MySQL (via environment variables)
    Django ORM

---

## Features:

    User Signup/Login/Logout
    Product Listings and Detail View
    Add to Cart & Quantity Updates
    Order Summary & Payment Page
    Admin Product Management
    Media & Static File Handling
    Environment Variables with dotenv

---

## Authentication

    Django’s built-in authentication
    Session-based login/logout

---

## File Uploads

Media files (like images) are uploaded to /media/ and served using Django's MEDIA_URL.

---

## Run Locally

    1. Clone the repository:
    
    git clone https://github.com/your-username/e-paan-store.git
    cd e-paan-store
    
    2. install dependencies:
    
    pip install -r requirements.txt
    
    
    3. Setup .env:
    
    DB_NAME=your_db
    DB_USER=your_user
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=3306
    
    4. Run migrations:
    
    python manage.py migrate
    
    5. Start the server:
    
    python manage.py runserver

---

## Folder Structure Highlights

    shop/
    │
    ├── shop/                # Django project settings
    ├── user1/               # Main app handling views, models, templates
    │   ├── templates/
    │   │   ├── app/         # Pages like home, menu, about, cart etc.
    │   │   └── auth/        # Login and Signup pages
    ├── static/              # CSS & JS files
    ├── media/               # Uploaded product images
    ├── .env                 # Environment variables
    ├── manage.py

---

## Status
Project is fully functional and ready for extension, deployment, or integration with payment APIs and admin dashboards.
