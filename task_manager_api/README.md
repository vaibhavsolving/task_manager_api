# Task Manager Backend API

A production-style **REST API** built with Django & Django REST Framework, featuring JWT authentication, task CRUD, filtering, pagination, and proper error handling.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Language |
| Django 4.2 | Web framework |
| Django REST Framework | API layer |
| SimpleJWT | JWT authentication |
| SQLite | Database (dev) |
| python-dotenv | Environment variables |

---

## Project Structure

```
task_manager_api/
├── task_manager_api/       # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                  # Main app
│   ├── models.py           # Task model
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views
│   ├── urls.py             # App routes
│   └── admin.py            # Admin config
├── manage.py
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/task-manager-api.git
cd task_manager_api
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create superuser (optional, for admin panel)
```bash
python manage.py createsuperuser
```

### 7. Start the development server
```bash
python manage.py runserver
```

API is now running at: `http://127.0.0.1:8000/`

---

## API Endpoints

### Auth

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | Login, get tokens | No |
| POST | `/api/auth/refresh/` | Refresh access token | No |
| POST | `/api/auth/logout/` | Logout (blacklist token) | Yes |
| GET | `/api/auth/me/` | Get current user profile | Yes |

### Tasks

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/tasks/` | List all your tasks | Yes |
| POST | `/api/tasks/` | Create a new task | Yes |
| GET | `/api/tasks/<id>/` | Get a specific task | Yes |
| PUT | `/api/tasks/<id>/` | Full update a task | Yes |
| PATCH | `/api/tasks/<id>/` | Partial update a task | Yes |
| DELETE | `/api/tasks/<id>/` | Delete a task | Yes |

---

## Postman Examples

### Register
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "john",
  "email": "john@example.com",
  "password": "securepass123",
  "password_confirm": "securepass123"
}
```

**Response:**
```json
{
  "message": "Registration successful.",
  "user": { "id": 1, "username": "john", "email": "john@example.com" },
  "tokens": {
    "access": "eyJ...",
    "refresh": "eyJ..."
  }
}
```

---

### Login
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "john",
  "password": "securepass123"
}
```

---

### Create Task
```http
POST /api/tasks/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "title": "Build the login page",
  "description": "Create JWT-based login UI",
  "status": "pending",
  "priority": "high",
  "due_date": "2025-03-01"
}
```

---

### List Tasks (with filters)
```http
GET /api/tasks/?status=pending&priority=high&search=login&ordering=-created_at
Authorization: Bearer <your_access_token>
```

**Query Parameters:**
- `status` → `pending` | `in_progress` | `completed`
- `priority` → `low` | `medium` | `high`
- `search` → searches title & description
- `ordering` → `created_at`, `due_date`, `priority`, `status` (prefix `-` for descending)
- `page` → page number (10 items per page)

---

### Update Task Status
```http
PATCH /api/tasks/1/
Authorization: Bearer <your_access_token>
Content-Type: application/json

{
  "status": "completed"
}
```

---

## Task Model Fields

| Field | Type | Options |
|-------|------|---------|
| `title` | string | Required, min 3 chars |
| `description` | string | Optional |
| `status` | choice | `pending`, `in_progress`, `completed` |
| `priority` | choice | `low`, `medium`, `high` |
| `due_date` | date | Optional, cannot be in the past |

---

## Features

- **JWT Auth** — Access & refresh tokens, token blacklisting on logout
- **User isolation** — Users can only see/edit their own tasks
- **Validation** — Title length, due date, password match, unique email
- **Pagination** — 10 items per page by default
- **Filtering** — Filter by `status`, `priority`
- **Search** — Full-text search on `title` and `description`
- **Ordering** — Sort by any field, ascending or descending
- **Clean responses** — Consistent JSON with `message` keys

---

## Git Commit History

```
feat: initial django project setup
feat: task CRUD APIs
refactor: improve API structure
docs: add README and setup steps
```

---

## License

MIT
