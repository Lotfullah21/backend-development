# What is a Django App?

A Django app is a self-contained component within a Django project that performs a specific functionality or serves a particular purpose. Apps can be reused across projects and are designed to be modular, making it easier to maintain and extend Django projects.

To create a django app

```py
cd project-directory-name
django-admin startapp myapp
```

This command will create a new directory named myapp containing the necessary files and folders for your Django app.

Let's take a closer look at each of these files and directories.

## File descriptions

1. **ini**.py
   The **init**.py file is an empty file that tells Python to treat the myapp directory as a Python package. It's not necessary to add any code to this file unless you want to perform additional setup when the app is imported.

2. admin.py
   The admin.py file is where you can register models to be managed via Django's built-in admin interface. You can define custom admin views, filters, and actions for your models in this file.

3. apps.py
   The apps.py file defines the configuration for the Django app. It includes metadata such as the app name, verbose name, and app configuration class.

4. migrations/
   The migrations/ directory contains database migration files generated by Django's migration system. Migrations are used to manage changes to the database schema over time.

5. models.py
   The models.py file is where you define the data models for your Django app. Each model represents a database table, and you can define fields, relationships, and methods on the models to interact with the database.

6. tests.py
   The tests.py file is where you write tests for your Django app using Django's testing framework. Writing tests helps ensure the correctness and reliability of your application.

7. views.py
   The views.py file contains the view functions or classes that handle HTTP requests and return HTTP responses. Views are the heart of a Django app and define the logic for rendering templates, processing form submissions, and interacting with models.

## Project root files

When you create a new Django project, it generates a directory with several files and subdirectories.

`Manage.py`: A command-line utility for managing various aspects of the project, such as running the development server, applying migrations, and creating new apps.

`<project-name>`: This directory carries the name you provided when you created the project. Inside, you'll find:

`(a) 'settings.py'`: This file holds the project's configuration settings, including database configurations, installed apps, middleware, and more.

`(b) 'urls.py'`: The urls.py files define the URL patterns and their corresponding views. These patterns determine which view should be called when a particular URL is accessed.

`(c) 'wsgi.py' and 'asgi.py':` This file is used for deploying the Django project on a WSGI server and ASGI server respectively.

`(d) **init**.py:`` An empty file indicating that the directory should be treated as a Python package.

`requirements.txt`

When you run pip freeze > requirements.txt , you're essentially creating a file named requirements.txt that contains a list of all the installed packages and their versions in the current environment. This file can be shared with others, allowing them to replicate your environment by running pip install -r requirements.txt.

## app

an app is a self-contained module that encapsulates a specific piece of functionality or a related set of features within a larger project. Each app is designed to do one thing and do it well, making it easier to organize and maintain your code.
they do not depend on other apps to work

```sh
django-admin startapp users
or
python manage.py startapp <name of app>
```

## project

A Django project is a Python package containing the database configuration used by various sub-modules (Django calls them apps) and other Django-specific settings.

```sh
django-admin startproject demoproject
```

## runserver

This command starts Django’s built-in development server on the local machine with IP address 127.0.0.1 and port 8000.

```sh
python manage.py runserver
```
