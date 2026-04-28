# 🚀 Expense Tracker Backend

## 📌 Overview

This backend service powers the Expense Tracker application by providing secure and scalable REST APIs for authentication and expense management. It ensures that each user can manage their own financial data independently and securely.

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* JWT Authentication
* SQLite
* Render (Deployment)

---

## 🔐 Core Features

* Secure user authentication using JWT
* User registration and login system
* Full CRUD operations for expenses
* Category and date-based filtering
* User-specific data isolation
* RESTful API architecture

---

## 📂 Project Structure

```id="struct001"
backend/
│
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── accounts/         
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── expenses/          
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
└── requirements.txt
```

---

## 🔐 Authentication

### Features:

* User Registration
* User Login
* JWT Token generation

### Endpoints:

* POST `/api/accounts/register/`
* POST `/api/accounts/login/`

---

## 💰 Expense Management API

### Endpoints:

* GET `/api/expenses/`
* POST `/api/expenses/`
* PUT `/api/expenses/{id}/`
* DELETE `/api/expenses/{id}/`

### Filters:

* `/api/expenses/?category=food`
* `/api/expenses/?date=YYYY-MM-DD`

---

## ⚙️ Setup Instructions

### Clone repo

```id="cmd101"
git clone https://github.com/sai0566/expense_tracker.git
cd backend
```

### Create environment

```id="cmd102"
python -m venv env
env\Scripts\activate
```

### Install dependencies

```id="cmd103"
pip install -r requirements.txt
```

### Run project

```id="cmd104"
python manage.py migrate
python manage.py runserver
```

---

## 🌐 Deployment

* Hosted on Render
* Live API: https://expense-backend-ve9q.onrender.com/

---

## 🧠 Key Highlights

* Modular architecture (accounts + expenses)
* Secure token-based authentication
* Efficient filtering and query handling
* Scalable backend design

---

## 🚀 Future Enhancements

* Password reset & email verification
* Pagination and search
* CSV/PDF export
* Advanced analytics APIs

---

## 👤 Author

Sree venkata satya sai ram
