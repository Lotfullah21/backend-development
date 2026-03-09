# Django Setup and Essentials

## 1) Create and activate a virtual environment

Using a virtual environment keeps project dependencies isolated.

Create:

```bash
python3 -m venv .venv
```

Activate (macOS/Linux):

```bash
source .venv/bin/activate
```

Activate (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Upgrade packaging tools (recommended):

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 2) Install Django

```bash
pip install django
```

Optional: freeze dependencies

```bash
pip freeze > requirements.txt
```

## 3) Create a new Django project

```bash
django-admin startproject project_name
```

```bash
django-admin startproject project_name .
```

It avoids creating sub directories for a project.

### Command structure: `django-admin` vs `manage.py`

Both run Django commands, but they are used at different times.

`django-admin` command structure:

```bash
django-admin <command> [options]
```

Examples:

```bash
django-admin startproject project_name
django-admin help
```

What it does:

- Global Django command-line utility
- Mainly used before a project exists
- Common use: create a new project with `startproject`

`manage.py` command structure:

```bash
python manage.py <command> [options]
```

Examples:

```bash
python manage.py runserver
python manage.py startapp users
python manage.py makemigrations
python manage.py migrate
python manage.py test
```

What it does:

- Project-specific command runner
- Uses your project settings automatically
- Preferred after project creation for daily development

Quick difference:

| Tool           | Typical use                                        |
| -------------- | -------------------------------------------------- |
| `django-admin` | Global commands, especially creating a new project |
| `manage.py`    | Commands inside an existing project                |

## 4) Run the development server

```bash
python manage.py runserver
```

Default URL: `http://127.0.0.1:8000/`

## 5) Create an app

```bash
python manage.py startapp users
```

Then register it in `config/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    "users",
]
```

## Naming conventions

Use simple, predictable names:

- Project package: `config`, `core`, or project name (lowercase)
- App names: short, singular domain names like `user`, `account`, `blog`, `payment`
- Python modules: lowercase with underscores (`snake_case`)
- Classes: `PascalCase` (example: `UserProfile`)

Avoid:

- Spaces or hyphens in module/app names
- Very generic app names like `app` or `main` in large projects

## Essential Django commands

```bash
# Create migrations based on model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create an admin user
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Run tests
python manage.py test
```

## Typical first-day workflow

1. Create and activate virtual environment.
2. Install Django.
3. Create project with `startproject`.
4. Create first app with `startapp`.
5. Add app to `INSTALLED_APPS`.
6. Build models, run `makemigrations` and `migrate`.
7. Run server and start implementing views/URLs/templates.
