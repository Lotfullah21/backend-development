## Postgres

- Install postgres

[postgres](https://www.postgresql.org/download/)
[pg-admin](https://www.postgresql.org/ftp/pgadmin/pgadmin4/v8.11/macos/)

pg-admin to view the tables inside the database.

## How to connect postgresql to django?

- Open virtual env
- `pip install psycopg2-binary`
- cd firstProject

```sh
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': ‘<database_name>’,
       'USER': '<database_username>',
       'PASSWORD': '<password>',
       'HOST': '<database_hostname_or_ip>',
       'PORT': '<database_port>',
   }
}
```

- python manage.py migrate
- python manage.py runserver

[How-to-connect](https://www.geeksforgeeks.org/how-to-use-postgresql-database-in-django/)

## MySql

## How to connect mysql to django?

[How-to-connect](https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/)

## CRUD operations

Use `create()` when you want to quickly create and save a new instance without additional processing.
`create()` method is a shortcut that both creates the object and saves it to the database in one step.

```sh
new_student = Student(name="ali", gender="Male", email="ali@gmail.com", date_of_birth="1998-02-01")
new_student.name = new_student.name.upper()  # Modify the object before saving
new_student.save()
```

Use `save()` when you need to perform additional operations on the instance before saving or when updating an existing instance.
If you are using other models inside other modes, make sure to create other models first.

```sh
 python manage.py shell
```

1. Create an instance

```sh
new_student = Student(name="ali",gender="Male", email="ali@gmail.com", date_of_birth="1998-02-01")
new_student.save()
```

```sh
student1 = Student.object.create(name="ahmad", gender="Male", email="ahmad@gmail.com" ,date_of_birth="1998-02-01")
```

Using dict unpacking feature.

```sh
args = {"name": "ahmad", "gender": "Male", "email": "ahmad@gmail.com", "date_of_birth": "1998-02-01"}
Student.objects.create(**args)

```

use `CTRL+l` to clear the shell

2. Read

```sh
>>> new_student.save()
student = Student.objects.all()
student = Student.objects.get(id=1)
student # <Student: ali>
student.name # 'ali'
for s in student:
    print(f"{s.name} {s.date_of_birth} {s.email}")
male_student = Student.objects.filter(gender="Male")
for s in male_student:
    print(f"{s.name} {s.date_of_birth} {s.email}")

```

#### get_or_create()

```py
# Using get_or_create to find or create a student
student, created = Student.objects.get_or_create(
    email="ahmad@gmail.com",  # Searching by email
    defaults={
        "name": "Ahmad",
        "gender": "Male",
        "date_of_birth": "1998-02-01"
    }
)

if created:
    print("A new student was created:", student)
else:
    print("Retrieved existing student:", student)

```

if the field is present, get it, if not create it.

```shell
dep = Department.objects.last()
dep = Department.objects.first()
```

3. Update

Get the object and change its property, but note down that always use `instance_name.save()` to save the changes database.

```sh
student = Student.objects.get(id=4)
student.name="Fatima"
student.name # 'Fatima'
```

4. Delete

```sh
student = Student.objects.get(name="ali")
student.delete()
(1, {'home.Student': 1})
# To delete all instances
students = Student.objects.all()
students.delete()
```
