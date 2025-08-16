
# Django Concepts & Architecture – Code Institute Style (Theory Companion)

---

## 🧠 The Django MVT Pattern

### Model - View - Template

| Component | Role |
|----------|------|
| **Model** | Handles data and database structure (ORM layer) |
| **View** | Processes logic, fetches data, connects models to templates |
| **Template** | Renders HTML with context from views |

Django is **not MVC**, but close:
- **View (Django)** = Controller (traditional)
- **Template** = View (HTML layer)

---

## 🌐 Request-Response Cycle

1. User requests a URL.
2. Django finds a match in `urls.py`.
3. Matching **view** is called.
4. View fetches/updates data via **models**.
5. View passes data into a **template**.
6. **Template renders HTML**, returned to user.

---

## 📁 Django Project Structure

```bash
myproject/
├── manage.py
├── myproject/           # Settings, URLs, WSGI
│   ├── settings.py
│   ├── urls.py
├── app1/                # Your Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/app1/
│   ├── forms.py
│   └── admin.py
```

> 🧩 One project can have many apps. Keep apps modular.

---

## 🔗 URL Routing

**Project-level `urls.py`:**
```python
from django.urls import path, include

urlpatterns = [
    path('', include('app1.urls')),
]
```

**App-level `urls.py`:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
```

---

## 📄 Templates & Context

Views pass **context dictionaries** to templates:
```python
context = {'bookings': Booking.objects.all()}
return render(request, 'bookings/list.html', context)
```

> Use `{% for booking in bookings %}` in the template.

Template engines support:
- `if`, `for`, `block`, `extends`, `include`
- Filters like `|date`, `|default`, `|length`

---

## 🧩 Models & Relationships

### Best Practices:
- Always define `__str__()` for readability.
- Use `related_name` in `ForeignKey`.
- Use `Meta` for ordering.
- Use validators or `clean_<field>()` in forms.

---

## 🔁 Class-Based vs Function-Based Views

| Type | When to Use |
|------|-------------|
| **CBV (Preferred)** | For standard CRUD operations using built-in Django views |
| **FBV** | For simple logic or one-off views with custom flow |

> CBVs use `ListView`, `DetailView`, `CreateView`, etc.

---

## ⚙️ Forms vs ModelForms

| Type        | Use When...                            |
|-------------|----------------------------------------|
| `forms.Form`      | Form fields not tied to a model      |
| `forms.ModelForm` | Creating/editing model instances     |

Always override `__init__()` for styling and add widgets as needed.

---

## 📬 Messages Framework

Used for status updates:
```python
from django.contrib import messages
messages.success(request, "Booking confirmed.")
```

Template:
```html
{% for message in messages %}
  <div>{{ message }}</div>
{% endfor %}
```

---

## 🔐 Authentication System

Built-in views and forms:
- Login, logout, registration
- Password reset flow
- `LoginRequiredMixin` to protect views

Use `request.user` in views or templates to access current user.

---

## 🔒 Permissions and Security

- Only logged-in users should access CRUD features.
- Hide buttons/links from unauthenticated users.
- Always check ownership before editing/deleting data.
```python
if booking.user != request.user:
    return HttpResponseForbidden()
```

---

## 🧪 Testing Strategy

- Manual testing: Document expected vs actual result.
- Automated testing: Use `unittest.TestCase` or `TestCase` from Django.
- Test forms, views, models, templates separately.

---

## 📦 Project Structure Tips

- One function = one purpose
- Split forms, views, templates into logical files
- Use `utils.py` for reusable logic
- Use `base.html` + `{% extends %}` for all templates
- Use `crispy_forms` or bootstrap classes for better UX

---

## ✅ Summary: What Makes a Good Django Project

- MVT pattern clearly followed
- Templates well-structured with inheritance
- Context passed cleanly from views
- CBVs used where possible
- Forms use clean and user-friendly inputs
- Messages and feedback for all actions
- Authentication is clear and secure
- Static and media files configured
- Deployment uses environment variables and is secure
- README documents everything
