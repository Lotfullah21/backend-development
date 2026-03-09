### Migrations

migrations records changes made to models and implements theses changes to the database schema.

## Migrations

Records changes made to models and implements these changes to the database schema.
Django translates the models into respective database tables in the backend database with a mechanism known as migration. It also propagates any changes in the model structure such as adding, modifying or removing a field attribute of a model class to the mapped table.
Django migrations allow us to add, modify, and delete models or fields without needing to manually alter our database.

Django’s migration is a version control system. Whenever you add a new model or effect changes in an existing model, you need to run the `makemigrations` command. It creates a script for making changes in the mapped table. Every time you run the `makemigrations` command and Django detects the changes, a script with its name and version number is created. To implement the changes according to the migration script, you need to run the `migrate` command

## 1. `python manage.py makemigrations`

The migration script is a set of instructions on what models to create against the database.

#### Purpose:

This command creates migration files based on changes you’ve made to your models (in models.py), in other words it prepare the changes to be made to the model.

#### What it does:

It detects changes to the models in your Django app, such as creating new models, modifying fields, or deleting models/fields.
It generates new migration files that contain the necessary information to alter the database schema. These migration files are Python files that describe the changes in a way Django can apply them later.

#### What it doesn’t do:

It does not make any changes to the actual database. It only prepares the changes and stores them in migration files.

#### Example:

If you add a new model or field in models.py, running ` python manage.py makemigrations` will generate a migration file like `0002_auto_20211006_1523.py`, which contains the instructions to add that model or field to the database.

## 2. `python manage.py migrate`

### Purpose:

This command applies the migration files to the actual database, altering the database schema according to the instructions in the migration files.

### What it does:

It executes the migrations created by makemigrations by running the necessary SQL commands to modify the database schema.
It applies the changes to the database, such as creating new tables, adding or modifying fields, or removing models/tables.

#### What it doesn’t do:

It does not generate new migration files. It only applies existing migration files to the database.

#### Example:

After running python manage.py makemigrations, if you run python manage.py migrate, it will apply the changes in the migration file to the database, like creating new tables or adding columns.

```sh
python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate
# shows sql command
manage.py sqlmigrate myapp
```

Django will automatically translate our Python model into the necessary SQL to create the tables in the database.

## using custom sql

```sql
CREATE TABLE user(
    "id" serial NOT NULL PRIMARY KEY
    "first_name" varchar(30) NOT NULL
    "last_name" varchar(30) NOT NULL
)
```

| Command                           | What it does                                           | What it doesn’t do                  |
| --------------------------------- | ------------------------------------------------------ | ----------------------------------- |
| `python manage.py makemigrations` | Detects changes to models and creates migration files  | Does not modify the database        |
| `python manage.py migrate`        | Applies migration files and alters the database schema | Does not create new migration files |

## schema

a schema is a blueprint or structure that defines how data is organized and how the relationships among different entities are managed within a database.

A schema

- specifies the tables in a database, fields in table
- determines the relationship between the tables, one-to-many, one-to-one, many-to-many
