# Django `settings.py` Explained

## What is `settings.py`?

`settings.py` is the main configuration file for a Django project.
It controls how your project behaves in development and production.

Django loads it at startup, and many commands (`runserver`, `migrate`, `test`) depend on it.

## Where is it?

After:

```bash
django-admin startproject config .
```

you usually get:

```text
config/
├─ __init__.py
├─ settings.py
├─ urls.py
├─ asgi.py
└─ wsgi.py
```

## Common sections in a default `settings.py`

## 1) Path setup

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
```

- `Path`: helps build safe filesystem paths
- `BASE_DIR`: points to your project root and is reused in database/static/media paths

## 2) Security and debug

```python
SECRET_KEY = "..."
DEBUG = True
ALLOWED_HOSTS = []
```

- `SECRET_KEY`: used for cryptographic signing; keep private
- `DEBUG`: should be `False` in production
- `ALLOWED_HOSTS`: domains/IPs allowed to serve your app

## 3) Installed apps

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- Enables Django built-in apps and your own apps (for example, `"users"`, `"blog"`)
- If an app is missing here, Django will not load it

## 4) Middleware

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

- Middleware runs on each request/response
- Handles things like security headers, sessions, auth, CSRF protection

## 5) URL and app entry points

```python
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
```

- `ROOT_URLCONF`: top-level URL configuration module
- `WSGI_APPLICATION`: entry point for WSGI servers

You may also see:

```python
ASGI_APPLICATION = "config.asgi.application"
```

- Entry point for ASGI servers (async support)

## 6) Templates

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": [...]},
    }
]
```

- `BACKEND`: template engine backend
- `DIRS`: global template folders (example: `BASE_DIR / "templates"`)
- `APP_DIRS`: also load templates from each app's `templates/` folder
- `context_processors`: inject common data into templates (request, auth, messages, etc.)

## 7) Database

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

- Defines database connection settings
- Default uses SQLite for local development
- For production, often replaced with PostgreSQL/MySQL config

## 8) Password validation

```python
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
```

- Rules for user password strength and safety

## 9) Internationalization and time

```python
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
```

- `LANGUAGE_CODE`: default language
- `TIME_ZONE`: app timezone
- `USE_I18N`: translation support
- `USE_TZ`: timezone-aware datetimes

## 10) Static and media files

```python
STATIC_URL = "static/"
MEDIA_URL = "media/"
```

Common additional settings:

```python
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"
```

- `STATIC_URL`: URL prefix for static assets (CSS/JS/images)
- `STATICFILES_DIRS`: source static folders in development
- `STATIC_ROOT`: collected static files location for deployment
- `MEDIA_URL`/`MEDIA_ROOT`: user-uploaded file URL/path

## 11) Default primary key field type

```python
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

- Default type for auto-generated model primary keys

## Practical tips

1. Keep secrets and environment-specific values in environment variables.
2. Use separate settings for `development` and `production` in real projects.
3. Set `DEBUG = False` in production and configure `ALLOWED_HOSTS`.
4. Review security settings before deploying (`CSRF`, `SECURE_*`, HTTPS).
