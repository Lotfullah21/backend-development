# Django Learning Repository

This repository contains a small Django project and a set of topic-based notes covering core Django and backend concepts.

## Repository Overview

- `hlab/`: Django project source code
- `documents/`: learning notes and reference material

## Documentation Index

The main documentation lives under [`documents/`](./documents/).

- [Django introduction](./documents/01-intro-django/README.md)
- [Framework architecture](./documents/02-framework-architecture/README.md)
- [Views](./documents/03-views/Readme.md)
- [URL routing](./documents/03-views/url/Readme.md)
- [HTTP request and response](./documents/04-htttp/Readme.md)
- [Errors](./documents/05-errors/Readme.md)
- [Models](./documents/06-models/Readme.md)
- [Database notes](./documents/database/README.md)
- [Server concepts](./documents/server/README.md)
- [Templates](./documents/tempalte/README.md)
- [Static files](./documents/static-files/README.md)
- [Utilities and ORM notes](./documents/utils/README.md)
- [Forms](./documents/form/FORMS.MD)
- [Code samples](./documents/code-in-description/CODE.md)

## Django Project Structure

The runnable Django project is in [`hlab/`](./hlab/).

```text
hlab/
├── manage.py
├── db.sqlite3
├── hlab/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── courses/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── notifications/
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    └── views.py
```

## Getting Started

### Requirements

- Python 3.11 or newer
- `pip`

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django python-dotenv psycopg2-binary
cd hlab
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` after the server starts.

## Notes

- Some documentation folder names intentionally use the current on-disk names, such as `tempalte` and `04-htttp`, so the links in this README match the repository exactly.
