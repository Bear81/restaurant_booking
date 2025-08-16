
# Django Developer Reference – Code Institute Style

## 🧩 Models

### ✅ Basic Model Structure
```python
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
```

### ✅ Model Field Types
- `CharField(max_length=...)`: Short text
- `TextField()`: Long text
- `IntegerField()`, `DecimalField()`: Numbers
- `DateField()`, `TimeField()`, `DateTimeField()`
- `BooleanField()`
- `ImageField(upload_to='images/')`
- `ForeignKey()`, `ManyToManyField()`: Relationships

> 💡 **Use `choices=`** for dropdown menus and readable enums.

```python
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
]

status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
```

### ⚙️ Meta Class for Ordering
```python
class Meta:
    ordering = ['-date']
```

### 🔁 Model Relationships

#### ✅ One-to-Many (`ForeignKey`)
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

#### ✅ Many-to-Many
```python
tags = models.ManyToManyField('Tag')
```

---

## 🔍 Views

### ✅ Class-Based Views (Preferred)
```python
from django.views.generic import ListView, DetailView
from .models import Booking

class BookingListView(ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'
```

```python
class BookingDetailView(DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
```

> 💡 Override `get_queryset()` if you need to filter by user or custom logic.

### ✅ CBV + LoginRequiredMixin
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/my_bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
```

### ⚠️ Function-Based Views (FBVs)
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

### 🔄 Redirects & Messages
```python
from django.contrib import messages
from django.shortcuts import redirect

messages.success(request, "Booking successfully created.")
return redirect('booking_list')
```

---

## 📝 Forms

### ✅ Using ModelForm (Recommended)
```python
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'number_of_guests']
```

### ✨ Customising Form Fields
```python
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'placeholder': 'YYYY-MM-DD'
        })
```

```python
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'time': forms.TimeInput(attrs={'type': 'time'}),
    }
```

### ✅ Form Validation
```python
    def clean_number_of_guests(self):
        guests = self.cleaned_data.get('number_of_guests')
        if guests > 10:
            raise forms.ValidationError("Maximum 10 guests per booking.")
        return guests
```

---

## 📐 Templates

### ✅ Template Inheritance
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <title>{% block title %}Site Title{% endblock %}</title>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

```html
<!-- home.html -->
{% extends 'base.html' %}
{% block title %}Home{% endblock %}
{% block content %}
<h1>Welcome to the site</h1>
{% endblock %}
```

### ✅ Template Filters
```html
<p>Booking for {{ booking.date|date:"F j, Y" }}</p>
```

### ✅ Conditional Logic
```html
{% if user.is_authenticated %}
  <p>Hello, {{ user.username }}!</p>
{% else %}
  <p>Please log in.</p>
{% endif %}
```

### 🔁 Looping with `for`
```html
<ul>
{% for booking in bookings %}
  <li>{{ booking.date }} at {{ booking.time }}</li>
{% empty %}
  <li>No bookings found.</li>
{% endfor %}
</ul>
```

### 📩 Displaying Messages
```html
{% if messages %}
  <ul>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
  </ul>
{% endif %}
```

### 🧼 Static Files in Templates
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

## ✅ Summary Table

| Topic             | Best Practice                                                             |
|------------------|----------------------------------------------------------------------------|
| Forms            | Use `ModelForm`, override `__init__`, use widgets and validation methods  |
| Views            | Use CBVs with mixins, override `get_queryset()` if filtering needed       |
| Templates        | Use `{% extends %}`, `{% block %}`, handle messages, filters, loops       |
| Static files     | Always load via `{% load static %}` in templates                          |
