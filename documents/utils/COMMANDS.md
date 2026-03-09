## .gitgnore file

```sh
# To remove files from staged area
git rm -r --cached .
```

```sh
# Python
*.pyc
__pycache__/
*.pyo
*.pyd
*.env
*.DS_Store

# Virtual environment
env/
venv/
ENV/
venv.bak/


# Django specific
*.log
*.pot
*.pyc
*.mo
*.swp
db.sqlite3
db.sqlite3-journal
**/*.sqlite3
# Ignore all media and static files in all apps,** wildcard, matches any directory level
**/media/*
**/static/*

# Migrations (optional, you may want to include these)
**/migrations/*

# Ignore node_modules (if you're using JavaScript/React, etc.)
node_modules/

# Ignore IDE-specific files
.vscode/
.idea/

settings.py
```

### Setup for the project

```sh
# install python and pip using Homebrew
brew install python

# install virtualenv using pip
python3 -m pip install virtualenv

# make a main directory
mkdir directory_name
cd directory_name

# create a new virtual environment
virtualenv env

# activate virtual environment (macOS)
source env/bin/activate

# add .gitignore and requirements.txt
touch .gitignore
touch requirements.txt

# install Django in the virtual environment
pip install django
pip install python-dotenv

# check if Django is installed
django-admin --version
#
pip install -r requirements.txt
# create a new Django project (corrected command)
django-admin startproject project_name

# go to the project directory
cd project_name

# create an app inside the project
django-admin startapp appname
# or
python manage.py startapp appname

# start the development server
python manage.py runserver
```

```sh
<!-- to stop or remove a file from already committed file to github. -->
git rm -r --cached path/to/media/directory
```
