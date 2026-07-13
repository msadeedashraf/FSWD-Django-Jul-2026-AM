# Part 4 — Add Templates and Static Files

Now we will move from plain text to real HTML pages.

## Step 10. Create folders for templates and static files

Inside the same folder where `manage.py` exists, create:

```text
templates/
static/
```

Inside `static`, create:

```text
static/css/
static/scripts/
```

Your structure should look like this:

```text
myproject/
├── manage.py
├── templates/
└── static/
    ├── css/
    └── scripts/
```

---

## Step 11. Add CSS

Create:

```text
static/css/styles.css
```

Add:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
}

header, footer {
    background-color: #ff8500;
    color: white;
    padding: 20px;
    text-align: center;
}

main {
    padding: 30px;
}

.card {
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

a {
    color: #ff8500;
    text-decoration: none;
}
```

---

## Step 12. Add JavaScript

Create:

```text
static/scripts/myscript.js
```

Add:

```javascript
console.log("JobZila JavaScript loaded");
```

---

## Step 13. Create a shared layout template

Create:

```text
templates/sharedpage.html
```

Add:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}JobZila{% endblock title %}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header>
        <h1>JobZila</h1>
        <nav>
            <a href="/">Home</a> |
            <a href="/jobs/">Jobs</a> |
            <a href="/contact/">Contact</a>
        </nav>
    </header>

    {% block main %}
    {% endblock main %}

    <footer>
        <p>&copy; 2026 JobZila</p>
    </footer>

    <script src="{% static 'scripts/myscript.js' %}"></script>
</body>
</html>
```

This is the main layout. Other pages will reuse it.

---

## Step 14. Create the home page template

Create:

```text
templates/home.html
```

Add:

```html
{% extends 'sharedpage.html' %}

{% block title %}Home | JobZila{% endblock title %}

{% block main %}
<main>
    <section class="card">
        <h2>Find Your Next Job</h2>
        <p>Welcome to JobZila, a simple job board built with Django.</p>
        <p><a href="/jobs/">View Jobs</a></p>
    </section>
</main>
{% endblock main %}
```

---

## Step 15. Create the contact page template

Create:

```text
templates/contact.html
```

Add:

```html
{% extends 'sharedpage.html' %}

{% block title %}Contact | JobZila{% endblock title %}

{% block main %}
<main>
    <section class="card">
        <h2>Contact Us</h2>
        <p>Email us at support@jobzila.com</p>
    </section>
</main>
{% endblock main %}
```

---

## Step 16. Update views to render templates

Open:

```text
myproject/myproject/views.py
```

Replace the code with:

```python
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")
```

---

## Step 17. Update template settings

Open:

```text
myproject/myproject/settings.py
```

Find `TEMPLATES` and update `DIRS`:

```python
"DIRS": [BASE_DIR / "templates"],
```

Find `STATIC_URL` and add `STATICFILES_DIRS` below it:

```python
STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "static"]
```

Test again:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/contact/
```

---