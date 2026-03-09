# Models

To work with a database in a backend app, you have two options:

- **Raw SQL** — write queries directly against the database yourself.
- **Model (ORM)** — use a middle layer that translates Python code into SQL for you.

Django uses the second approach. A **model** is a Python class that represents a database table. Instead of writing SQL, you define your data structure in Python and Django handles the rest.

## Defining a Model

A model subclasses `django.db.models.Model`. Each attribute you define becomes a column in the table.

```python
# models.py
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=90)
    last_name  = models.CharField(max_length=90)
```

This creates a `User` table with two columns: `first_name` and `last_name`. Django also adds an `id` primary key column automatically.

- Each model maps to exactly one database table. Each instance of the model represents one row in that table.

After creating the model, make sure you add the app config to installed apps in settings.

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    # apps
    'courses.apps.CoursesConfig',
]
```

## Migrations

When you define or change a model, Django needs to update the database schema to match. This is done through **migrations**.

```sh
python manage.py makemigrations   # detect model changes → create migration files
python manage.py migrate          # apply migration files → update the database
```

| Command          | What it does                                   | What it doesn't do                  |
| ---------------- | ---------------------------------------------- | ----------------------------------- |
| `makemigrations` | Detects model changes, creates migration files | Does not touch the database         |
| `migrate`        | Applies migration files to the database        | Does not create new migration files |

Other useful migration commands:

```sh
python manage.py showmigrations                      # list all migrations and their status
python manage.py sqlmigrate courses 0001_initial     # show the SQL a migration would run
```

- Think of migrations as a version history of your database schema. Every change to a model gets recorded as a new migration file.

## CRUD Operations

Django gives you built-in methods to create, read, update, and delete records without writing SQL.

To do the CRUD through python shell

```sh
python manage.py shell
```

**Create:**

```python
user = User.objects.create(first_name="John", last_name="Doe")
```

**Read:**

```python
user  = User.objects.get(id=1)     # one record — raises error if not found
users = User.objects.all()          # all records
```

**Update:**

```python
user = User.objects.get(id=1)
user.first_name = "Jane"
user.save()
```

**Delete:**

```python
user = User.objects.get(id=1)
user.delete()
```

## Schema

A **schema** is the blueprint of your database — it defines what tables exist, what columns each table has, and how tables relate to each other.

When you define a Django model, you are defining the schema in Python. After running `migrate`, the equivalent SQL is generated automatically. For reference, the SQL Django would produce for the `User` model above looks like:

```sql
CREATE TABLE user (
    "id"         serial       NOT NULL PRIMARY KEY,
    "first_name" varchar(90)  NOT NULL,
    "last_name"  varchar(90)  NOT NULL
);
```

A schema also defines relationships between tables:

- one-to-many (e.g. one author, many books)
- one-to-one (e.g. one user, one profile)
- many-to-many (e.g. many students, many courses)
