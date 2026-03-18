# Migrations

Migrations are Django's way of tracking changes you make to your models and applying those changes to the database. Think of it as **version control for your database schema**.

Every time you add a model, change a field, or delete something — Django can detect that and generate the SQL needed to update your database.

![Migration Flow](assets/migration-flow.svg)

## The two-step process

There are only two commands you need to remember:

### Step 1: `makemigrations` — detect changes

```sh
python manage.py makemigrations
```

This scans your `models.py` files, compares them to the previous migration files, and generates a new migration file describing what changed.

```
Migrations for 'courses':
  courses/migrations/0001_initial.py
    - Create model Course
    - Create model Student
```

- This does **not** touch the database. It only creates a Python file with instructions.

### Step 2: `migrate` — apply changes

```sh
python manage.py migrate
```

This reads the migration files and runs the actual SQL against your database — creating tables, adding columns, etc.

```
Applying courses.0001_initial... OK
```

- This is the step that modifies your database.

## What a migration file looks like

When you run `makemigrations`, Django creates a file like `0001_initial.py` inside your app's `migrations/` folder:

```
courses/
└── migrations/
    ├── __init__.py
    ├── 0001_initial.py      <- first migration
    └── 0002_add_age.py      <- next change
```

Each file is numbered sequentially. Django uses these numbers to know the order in which to apply changes.

## Useful commands

### See which migrations have been applied

```sh
python manage.py showmigrations
```

Output:

```
courses
 [X] 0001_initial       <- applied
 [ ] 0002_add_age       <- not yet applied
```

### See the SQL a migration will run

```sh
python manage.py sqlmigrate courses 0001
```

Output:

```sql
CREATE TABLE "courses_course" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(100) NOT NULL
);
```

- This is great for learning — you can see exactly what Django does behind the scenes.

## Common workflow

```sh
# 1. Edit your model
# 2. Generate the migration
python manage.py makemigrations

# 3. Check what will run (optional)
python manage.py sqlmigrate myapp 0001

# 4. Apply it
python manage.py migrate
```

## When do you need to run migrations?

Run `makemigrations` + `migrate` whenever you:

- Create a new model
- Add, remove, or rename a field
- Change a field's type or options (e.g., `max_length`, `null`, `default`)
- Add or change a relationship (`ForeignKey`, `ManyToManyField`, etc.)

## Quick reference

| Command                             | What it does                                   |
| ----------------------------------- | ---------------------------------------------- |
| `python manage.py makemigrations`   | Detects model changes, creates migration files |
| `python manage.py migrate`          | Applies migration files to the database        |
| `python manage.py showmigrations`   | Lists all migrations and their applied status  |
| `python manage.py sqlmigrate app N` | Shows the SQL that a migration will execute    |
