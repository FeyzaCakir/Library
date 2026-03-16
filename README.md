# 📚 Flask Library Management System

A **Flask-based library management web application** that allows users to manage books in a library system.
The application demonstrates **backend-oriented web development concepts** such as ORM usage, authentication, form validation, and CRUD operations.

The system is built using **Flask, SQLAlchemy ORM, Flask-WTF forms, and Flask-Login authentication**.

---

# 🚀 Core Features

* Book management (Create, Read, Update, Delete)
* User authentication system
* Form validation using Flask-WTF
* Secure password hashing with Bcrypt
* Session management using Flask-Login
* ORM-based database operations with SQLAlchemy

---

# 🧱 System Architecture

The project follows a **modular Flask architecture** to separate concerns:

```
library-management/
│
├── app.py            # Application entry point & route definitions
├── models.py         # SQLAlchemy database models
├── forms.py          # Flask-WTF form classes
├── extensions.py     # Shared extensions (SQLAlchemy instance)
│
├── templates/        # Jinja2 templates
│   ├── index.html
│   ├── add_book.html
│   ├── edit_book.html
│   ├── login.html
│   └── register.html
│
└── library.db        # SQLite database
```

---

# 🛠 Technologies

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Flask         | Web framework                       |
| SQLAlchemy    | ORM for database operations         |
| SQLite        | Relational database                 |
| Flask-WTF     | Form handling and validation        |
| Flask-Login   | Authentication & session management |
| Flask-Bcrypt  | Password hashing                    |
| Jinja2        | HTML template rendering             |
| python-dotenv | Environment variable management     |

---

# ⚙️ Application Configuration

The application is configured in **app.py**.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

### Key Configuration Details

* **SQLALCHEMY_DATABASE_URI** → Defines SQLite database location
* **SQLALCHEMY_TRACK_MODIFICATIONS** → Disabled to reduce memory overhead
* **SECRET_KEY** → Loaded from environment variables for session security

Database tables are automatically created during application startup:

```python
with app.app_context():
    db.create_all()
```

---

# 🗄 Database Schema

The application uses **SQLAlchemy ORM models**.

## Book Model

```
Book
│
├── id (Integer, Primary Key)
├── title (String, Required)
├── author (String, Required)
├── category (String, Optional)
├── publisher (String, Optional)
└── stock (Integer, Default=1)
```

Example model definition:

```python
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, default=1)
```

---

## User Model

Authentication users are stored in the **User** table.

```
User
│
├── id (Primary Key)
├── username (Unique)
├── email (Unique)
└── password (Hashed)
```

The model extends **UserMixin** from Flask-Login to provide authentication utilities.

---

# 🔐 Authentication System

Authentication is implemented using:

* **Flask-Login**
* **Flask-Bcrypt**

### Password Security

Passwords are hashed using Bcrypt:

```python
hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
```

During login:

```python
bcrypt.check_password_hash(user.password, form.password.data)
```

### Session Handling

Flask-Login manages user sessions using:

```
login_user(user)
logout_user()
current_user
@login_required
```

User loading function:

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

---

# 📑 Form Handling

Forms are implemented using **Flask-WTF**.

### BookForm

Used for adding books.

Fields:

* title
* author
* stock

### RegisterForm

Used for creating a new user account.

Fields:

* username
* email
* password

### LoginForm

Used for user authentication.

All forms use **WTForms validators** for input validation.

---

# 🔄 CRUD Operations

The application implements standard **CRUD operations** for book management.

## Create Book

```
POST /add
```

Creates a new book entry and stores it in the database.

---

## Read Books

```
GET /
```

Fetches all books using SQLAlchemy:

```python
books = Book.query.all()
```

---

## Update Book

```
POST /edit/<id>
```

Updates the selected book record.

---

## Delete Book

```
GET /delete/<id>
```

Removes the book from the database.

---

# ▶️ Running the Application

### 1. Clone the repository

```
git clone https://github.com/yourusername/library-management.git
cd library-management
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install flask flask-sqlalchemy flask-wtf flask-login flask-bcrypt python-dotenv
```

---

### 4. Create `.env` file

```
SECRET_KEY=your_secret_key
```

---

### 5. Run the application

```
python app.py
```

Application runs at:

```
http://127.0.0.1:5000
```

---

# 🎯 Technical Concepts Demonstrated

This project demonstrates practical usage of:

* Flask application architecture
* ORM-based database design with SQLAlchemy
* Authentication and session management
* Secure password hashing
* Form validation and CSRF protection
* CRUD application patterns
* Modular Flask project structure

---

# 🔮 Possible Improvements

Potential enhancements:

* Role-based authorization (Admin/User)
* REST API version using Flask RESTful
* Pagination for large book collections
* Search functionality
* Docker deployment
* PostgreSQL integration
