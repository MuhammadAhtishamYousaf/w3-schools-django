**Project Overview**

- **Name:** W3 Schools Django (sample project)
- **Purpose:** Demonstrate a minimal Django app with a `Members` model and basic CRUD operations using the Django ORM.

**Repository Structure**

- **`manage.py`:** Django command-line utility for this project.
- **`db.sqlite3`:** SQLite database created by Django migrations (local development only).
- **`members/`**: Django app that contains the application logic: models, views, templates, and migrations.
	- **`members/models.py`**: model definitions (see `Members`).
	- **`members/views.py`**: view functions and class-based views for the app.
	- **`members/templates/`**: HTML templates used by views (e.g., `myfirst.html`).
- **`my_tennis_club/`**: Django project configuration (settings, URLs, WSGI/ASGI).

**How this project was created**

1. Create a virtual environment and activate it.

```ps1
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install Django and create the project/app.

```ps1
pip install django
django-admin startproject my_tennis_club .
python manage.py startapp members
```

3. Add `members` to `INSTALLED_APPS` in `my_tennis_club/settings.py` and run migrations:

```ps1
python manage.py makemigrations
python manage.py migrate
```

4. Run the development server:

```ps1
python manage.py runserver
```

**How the code works — high level**

- Django project `my_tennis_club` contains global configuration (settings, URLs).
- The `members` app defines domain logic: `Members` model, views to handle requests, and templates for rendering HTML.
- Requests are routed via `my_tennis_club/urls.py` to app-level `members/urls.py` (if present) which calls view functions or class-based views.
- The ORM maps `Members` model instances to rows in the database (`db.sqlite3`).

**`Members` model summary**

The app defines a simple `Members` model at [members/models.py](members/models.py):

```py
class Members(models.Model):
		first_name = models.CharField(max_length=100)
		last_name = models.CharField(max_length=100)
		phone = models.IntegerField(max_length=13)
		joined_date = models.DateField(auto_now_add=True)

# Note: Django automatically adds an `id` AutoField primary key unless you define a custom primary key.
```

Important: `phone` is currently an `IntegerField` — consider using `CharField` to preserve leading zeros and support formatting.

**Common tasks & examples**

- Start shell: `python manage.py shell`
- Create a member:

```py
from members.models import Members
m = Members.objects.create(first_name='John', last_name='Doe', phone=1234567890)
print(m.id)  # id is the AutoField primary key
```

- Read examples:

```py
Members.objects.get(pk=1)
Members.objects.filter(first_name='John')
Members.objects.all()
```

- Update examples:

```py
m = Members.objects.get(pk=1)
m.last_name = 'Smith'
m.save()
Members.objects.filter(pk=1).update(last_name='Smith')
```

- Delete examples:

```py
m = Members.objects.get(pk=1)
m.delete()
Members.objects.filter(first_name='Obsolete').delete()
```

**Templates and Views**

- Simple templates live in `members/templates/` and are rendered by views in `members/views.py`.
- Example: `members/templates/myfirst.html` is an example template used in the app.

**Development checklist**

- Create and activate virtual environment (`.venv`).
- Install dependencies (`pip install django` or from `pyproject.toml` if using Poetry).
- Run `makemigrations` and `migrate`.
- Create a superuser for admin access: `python manage.py createsuperuser`.

**Next suggestions**

- Replace `phone = IntegerField` with `phone = CharField(max_length=20)`.
- Add `__str__` to `Members` for readable representations.
- Add app-level `urls.py` and examples of view routes in `members/views.py`.
- Add unit tests in `members/tests.py` to verify CRUD behavior.

If you'd like, I can make any of those suggestions now (update model, add URLs, add tests).
