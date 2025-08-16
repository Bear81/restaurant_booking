
# Django Developer Reference – Code Institute Style

## 🔐 Authentication & Permissions

### ✅ Built-in Auth System

- Use Django’s built-in `User` model for authentication.
- Login, logout, registration, and password reset use views from `django.contrib.auth`.

### ✅ User Registration (Custom Form Example)
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

---

### 🔑 LoginRequiredMixin for Views
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
```

> 💡 Always use `LoginRequiredMixin` for views requiring authentication.

---

### 🔐 Restricting Access in Templates
```html
{% if user.is_authenticated %}
  <a href="{% url 'logout' %}">Logout</a>
{% else %}
  <a href="{% url 'login' %}">Login</a>
{% endif %}
```

---

### 🛡 Role-Based Access
Check user status or groups:
```python
if request.user.is_superuser:
    # admin-only action
```

---

## 🧾 Static and Media Files

### ✅ Static Files (CSS/JS/Images)

**settings.py:**
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

**base.html:**
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

> Run `python manage.py collectstatic` before deployment.

---

### 📷 Media Files (User Uploads)

**settings.py:**
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**models.py:**
```python
image = models.ImageField(upload_to='uploads/')
```

**urls.py (dev only):**
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧪 Testing (Manual & Automated)

### ✅ Manual Testing Format (README)
```
Test Case: Booking form with valid data
Expected: Booking is saved, success message shown
Tested: Entered date, time, guests, clicked Submit
Result: Booking saved and user redirected
```

> 🔁 Repeat for each feature with valid & invalid flows.

---

### ✅ Unit Testing in Django
```python
from django.test import TestCase
from .models import Booking

class BookingModelTest(TestCase):
    def test_str_method(self):
        booking = Booking(name='Test', date='2025-01-01', time='12:00', number_of_guests=2)
        self.assertEqual(str(booking), 'Test - 2025-01-01 at 12:00:00')
```

- Place in `tests.py` or `tests/test_models.py`, etc.
- Run with `python manage.py test`

---

## 🛠 Deployment & Environment Config (Basics)

### ✅ Security Settings
```python
DEBUG = False
ALLOWED_HOSTS = ['yourapp.herokuapp.com']
```

> ⚠️ Never leave `DEBUG=True` in production!

---

### ✅ Environment Variables (Heroku / dotenv)
```python
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')
```

> Use `dj-database-url` and `python-decouple` or `.env` + `os.environ`.

---

### ✅ Files to Include
- `requirements.txt` (use `pip freeze > requirements.txt`)
- `Procfile`
```
web: gunicorn projectname.wsgi
```

- `.gitignore`: Ensure it includes:
```
.env
__pycache__/
*.sqlite3
/staticfiles/
/media/
```

---

## ✅ Final Summary of Best Practices

| Area              | Best Practice Summary                                                |
|-------------------|----------------------------------------------------------------------|
| Auth              | Use LoginRequiredMixin, check auth status in templates               |
| Static/Media      | Separate config for each, use `{% load static %}` in templates       |
| Testing           | Manual test cases in README, use unit tests for models/views/forms   |
| Security          | Use env variables, DEBUG=False, .gitignore secrets                   |
| Deployment        | Procfile, gunicorn, `collectstatic`, Heroku-compatible settings      |
