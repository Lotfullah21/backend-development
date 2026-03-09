# Model Naming Conventions

## Model class — singular, PascalCase

A model represents **one row**, so it should be singular:

```python
# correct
class Department(models.Model):
class Course(models.Model):
class StudentProfile(models.Model):

# wrong
class departments(models.Model):
class courses(models.Model):
```

Django auto-creates the table name as `appname_modelname` (e.g. `courses_department`).

## Fields — lowercase, snake_case

```python
# correct
name = models.CharField(max_length=100)
date_of_birth = models.DateField()
phone_number = models.CharField(max_length=15)

# wrong
Name = models.CharField(max_length=100)
dateOfBirth = models.DateField()
```

## Primary key — let Django handle it

Django adds `id = AutoField(primary_key=True)` automatically — an auto-incrementing integer (1, 2, 3, ...). Don't override it unless you have a specific reason.

```python
# correct — id is added for you
class Course(models.Model):
    name = models.CharField(max_length=100)

# unnecessary — forces you to manage IDs manually
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
```

## IDs in URLs — don't expose the integer `id`

Integer IDs are guessable (`/courses/42/` → try `/courses/43/`). For public-facing URLs, use a `SlugField` or `UUIDField` instead:

```python
# public content (courses, videos, blog posts) → slug
class Course(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)   # → /courses/django-for-beginners/

# private/sensitive resources (orders, payments) → UUID
import uuid
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # → /orders/550e8400-e29b-41d4-a716-446655440000/
```

| Approach     | URL                              | Best for                     |
| ------------ | -------------------------------- | ---------------------------- |
| Integer `id` | `/courses/42/`                   | Internal, admin only         |
| Slug         | `/courses/django-for-beginners/` | Public content, SEO          |
| UUID         | `/orders/550e8400-e29b...`       | Private, sensitive resources |

## ForeignKey — singular

The field holds **one** related object:

```python
# correct — each student has ONE department
department = models.ForeignKey(Department, on_delete=models.CASCADE)

# wrong — misleading, it is not many
departments = models.ForeignKey(Department, on_delete=models.CASCADE)
```

## ManyToManyField — plural

The field represents **many** related objects:

```python
# correct — a student has MANY courses
courses = models.ManyToManyField(Course)

# wrong — it is not one course
course = models.ManyToManyField(Course)
```

## `related_name` — plural

Describes what the reverse accessor returns:

```python
Class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="students")
# department.students.all() — reads naturally
```

## `CharField` always needs `max_length`

```python
# correct
name = models.CharField(max_length=100)

# wrong — will raise an error on most databases
name = models.CharField()
```

## `__str__` and `class Meta` go at the bottom

```python
class Course(models.Model):
    name     = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price    = models.PositiveIntegerField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
```

## Quick reference

| Thing             | Convention              | Example                    |
| ----------------- | ----------------------- | -------------------------- |
| Model class       | Singular, PascalCase    | `Course`, `StudentProfile` |
| Table name (auto) | `appname_modelname`     | `courses_course`           |
| Fields            | lowercase, snake_case   | `date_of_birth`            |
| Primary key       | Don't define it         | Django adds `id`           |
| ForeignKey field  | Singular                | `department`               |
| ManyToManyField   | Plural                  | `courses`                  |
| `related_name`    | Plural                  | `"students"`               |
| `CharField`       | Always set `max_length` | `max_length=100`           |
