
# 🛡️ Django REST API with Role-Based Access (User / Moderator / Admin)

A beginner-friendly Django REST Framework (DRF) project to manage users with 3 roles:

- **User** → Can create, view, update, and delete their own profile.
- **Moderator** → Can view, update, and delete any user.
- **Admin** → Can view, update, and delete users and moderators.

---

## 🧰 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (default)

---

## 🚀 Getting Started

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. 🐍 Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install django djangorestframework
```

### 4. ⚙️ Configure Settings

In `settings.py`, set the custom user model:

```python
AUTH_USER_MODEL = 'yourappname.User'
```

Replace `yourappname` with the name of your Django app (e.g., `core`, `accounts`, `main`).

---

## 🧪 Run the Project

### 1. 🛠️ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. 👤 Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

### 3. 🏁 Start the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin` to access the Django admin panel.

---

## 👥 Create Users with Roles

1. Login to the admin panel (`/admin`) using the superuser you just created.
2. Go to **Users** → **Add User**
3. Fill in:
   - Username
   - Password
   - Set `is_staff=True` (to allow login to admin)
   - Select `role`: `user`, `moderator`, or `admin`
4. Save

---

## 📡 API Endpoints

| Endpoint        | Method | Role Access           | Description                  |
|-----------------|--------|------------------------|------------------------------|
| `/users/`       | GET    | all (if staff)         | List users (limited by role) |
| `/users/`       | POST   | anyone                 | Create user account          |
| `/users/<id>/`  | GET    | self/mod/admin/mod     | View user details            |
| `/users/<id>/`  | PUT    | self/mod/admin         | Update user                  |
| `/users/<id>/`  | DELETE | self/mod/admin         | Delete user                  |

🔐 Auth: Login via browser or use session in Postman/cURL

---

## 🔑 Role Permissions Summary

| Role      | Create | Read | Update | Delete |
|-----------|--------|------|--------|--------|
| User      | ✅ self | ✅ self | ✅ self | ✅ self |
| Moderator | ❌     | ✅ all users | ✅ users | ✅ users |
| Admin     | ❌     | ✅ all | ✅ all | ✅ all |

---

## 🧪 Testing

You can test the API in:
- 🌐 Browsable API at `/users/`
- 🧪 Postman
- 🔐 Admin panel at `/admin`

---

## 📂 Project Structure

```
yourproject/
│
├── yourapp/
│   ├── models.py      # Custom User model
│   ├── serializers.py # User serializer
│   ├── views.py       # API views
│   ├── permissions.py # Custom role permissions
│   └── urls.py        # App URLs
│
├── yourproject/
│   └── settings.py    # Set AUTH_USER_MODEL here
│
├── db.sqlite3
└── manage.py
```

---

## 🤝 Contributions

PRs and improvements welcome! Let’s make it better for beginners together. 😊
