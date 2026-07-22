# Part 9 — Add User Registration and Login

## Step 32. Create users app

```powershell
py .\manage.py startapp users
```

---

## Step 33. Register users app

Open:

```text
myproject/myproject/settings.py
```

Add `users`:

```python
INSTALLED_APPS = [
    ...
    "jobs",
    "users",
]
```

---

## Step 34. Create users URLs

Create:

```text
users/urls.py
```

Add:

```python
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
```

---

## Step 35. Connect users URLs to project

Open:

```text
myproject/myproject/urls.py
```

Add:

```python
path("users/", include("users.urls")),
```

Full example:

```python
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("jobs/", include("jobs.urls")),
    path("blogs/", include("blogs.urls")),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("contact/", views.contact, name="contact"),
    path("users/", include("users.urls")),
]

```

---

## Step 36. Create registration and login views

Open:

```text
users/views.py
```

Add:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("jobs:job_list")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("jobs:job_list")
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("jobs:job_list")
```

---

## Step 37. Create registration template

Create this folder:

```text
users/templates/users/
```

Create:

```text
register.html
```

Add:

```html
{% extends 'sharedpage.html' %}

{% block title %}Register | JobZila{% endblock title %}

{% block main %}
<main>
    <section class="card">
        <h2>Create Account</h2>
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Register</button>
        </form>
    </section>
</main>
{% endblock main %}
```

---

## Step 38. Create login template

Create:

```text
users/templates/users/login.html
```

Add:

```html
{% extends 'sharedpage.html' %}

{% block title %}Login | JobZila{% endblock title %}

{% block main %}
<main>
    <section class="card">
        <h2>Login</h2>
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Login</button>
        </form>
    </section>
</main>
{% endblock main %}
```

Test:

```text
http://127.0.0.1:8000/users/register/
http://127.0.0.1:8000/users/login/
```

- Add this to the shared.html

```html
 {% if user.is_authenticated %}
        <a href="">Add Job</a> |
        <form method="POST" action="{% url 'users:logout' %}" style="display:inline;">
            {% csrf_token %}
            <button type="submit">Logout</button>
        </form>
    {% else %}
        <a href="{% url 'users:register' %}">Register</a> |
        <a href="{% url 'users:login' %}">Login</a>
    {% endif %}
```


```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}JobZila{% endblock title %}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  </head>
  <body>
    <header>
      <h1>JobZila</h1>

      <nav class="navbar">
        <button
          class="menu-toggle"
          type="button"
          aria-label="Open navigation menu"
          aria-expanded="false"
          aria-controls="main-menu"
        >
          ☰
        </button>

        <ul id="main-menu" class="nav-menu">
          <li><a href="{% url 'home' %}">Home</a></li>
          <li><a href="{% url 'jobs:job_list' %}">Find Jobs</a></li>
          <li><a href="{% url 'blogs:blogs' %}">Blogs</a></li>
          <li><a href="{% url 'terms' %}">Terms of Service</a></li>
          <li><a href="{% url 'privacy' %}">Privacy Policy</a></li>
          <li><a href="{% url 'contact' %}">Contact</a></li>

          {% if user.is_authenticated %}
        <a href="">Add Job</a> |
        <form method="POST" action="{% url 'users:logout' %}" style="display:inline;">
            {% csrf_token %}
            <button type="submit">Logout</button>
        </form>
    {% else %}
        <a href="{% url 'users:register' %}">Register</a> |
        <a href="{% url 'users:login' %}">Login</a>
    {% endif %}
        </ul>
      </nav>
    </header>

    <main>
      {% block main %}{% endblock main %}
    </main>

    <footer>
      <p>
        &copy; 2026 JobZila. All rights reserved.
        <a href="{% url 'contact' %}">Contact Us</a> |
        <a href="{% url 'terms' %}">Terms</a> |
        <a href="{% url 'privacy' %}">Privacy</a>
      </p>
    </footer>

    <script src="{% static 'js/menu.js' %}"></script>
  </body>
</html>

```