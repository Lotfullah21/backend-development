# Django Project and App Structure

## What is a Django project?

A Django **project** is the full web application container. It holds:

- Global settings
- URL routing at the top level
- Deployment entry points (ASGI/WSGI)
- One or more Django apps

Think of the project as the "whole system".

## What is a Django app?

A Django **app** is a focused module inside a project, usually for one domain or feature, for example:

- `users`
- `blog`
- `payments`

Apps are reusable and keep code organized. A project usually has multiple apps.

## Project vs app

- Project: global configuration and wiring
- App: specific business functionality

## Files created by `startproject`

Command:

```bash
django-admin startproject mysite
```

Typical structure:

```text
mysite/
├─ manage.py
└─ mysite/
   ├─ __init__.py
   ├─ settings.py
   ├─ urls.py
   ├─ asgi.py
   └─ wsgi.py
```

File purposes:

| File                 | Purpose                                                                         |
| -------------------- | ------------------------------------------------------------------------------- |
| `manage.py`          | Project command runner (`runserver`, `migrate`, `startapp`, etc.)               |
| `mysite/__init__.py` | Marks the folder as a Python package                                            |
| `mysite/settings.py` | Global config: database, installed apps, middleware, templates, static settings |
| `mysite/urls.py`     | Top-level URL routes and includes app routes                                    |
| `mysite/asgi.py`     | ASGI entry point (async servers)                                                |
| `mysite/wsgi.py`     | WSGI entry point (traditional Python web servers)                               |

## Files created by `startapp`

Command (run inside project root where `manage.py` exists):

```bash
python manage.py startapp blog
```

Typical structure:

```text
blog/
├─ __init__.py
├─ admin.py
├─ apps.py
├─ migrations/
│  └─ __init__.py
├─ models.py
├─ tests.py
└─ views.py
```

File purposes:

| File               | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| `blog/__init__.py` | Marks app folder as a Python package                         |
| `blog/admin.py`    | Register models for Django admin                             |
| `blog/apps.py`     | App config (`AppConfig`)                                     |
| `blog/migrations/` | Database schema history for this app                         |
| `blog/models.py`   | Data models (database tables/relations)                      |
| `blog/tests.py`    | Automated tests for the app                                  |
| `blog/views.py`    | Request/response logic (function-based or class-based views) |

## Important connection points

After creating an app:

1. Add app config to `INSTALLED_APPS` in `settings.py`.
2. Create app URLs (usually `app_name/urls.py`).
3. Include app URLs in project `urls.py`.
