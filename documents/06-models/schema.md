# Model Fields

A model's **fields** define the columns of the database table and what kind of data each column stores. Each field type enforces its own rules on what values are valid.

## Example Model

```python
# models.py
import uuid
from django.db import models

class Student(models.Model):
    name                 = models.CharField(max_length=100)
    gender               = models.CharField(max_length=10, choices=(("male", "Male"), ("female", "Female")), default="male")
    phone_number         = models.CharField(max_length=10, null=True, blank=True)
    email                = models.EmailField()
    date_of_birth        = models.DateField()
    student_registration = models.DateTimeField()
    profile_image        = models.ImageField(upload_to="images/students")
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)
    slug                 = models.SlugField(unique=True)
    uuid                 = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name
```

## Field Types

**`CharField`** — stores short text. `max_length` is required.

```python
name = models.CharField(max_length=100)
```

**`EmailField`** — like `CharField` but validates that the value is a valid email address.

```python
email = models.EmailField()
```

**`DateField`** — stores a date (year, month, day). No time.

```python
date_of_birth = models.DateField()
```

**`DateTimeField`** — stores both date and time.

```python
student_registration = models.DateTimeField()
```

**`ImageField`** — stores the path to an uploaded image file. `upload_to` sets the subfolder inside your media directory.

```python
profile_image = models.ImageField(upload_to="images/students")
```

- Requires the `Pillow` package: `pip install Pillow`

**`SlugField`** — stores a URL-friendly string (letters, numbers, hyphens, underscores). Useful for building readable URLs.

```python
slug = models.SlugField(unique=True)
```

**`UUIDField`** — stores a universally unique identifier. Setting `default=uuid.uuid4` generates one automatically. `editable=False` hides it from forms.

```python
uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
```

- `import uuid` must be at the top of `models.py` for this to work.

## Field Options

These can be added to any field.

**`max_length`** — maximum number of characters. Required for `CharField` and `SlugField`.

**`choices`** — restricts the field to a fixed set of values. Each choice is a tuple: `(stored_value, displayed_label)`.

```python
gender = models.CharField(
    max_length=10,
    choices=(("male", "Male"), ("female", "Female")),
    default="male",   # must match a stored value, not the label
)
```

- The first value in each tuple (`"male"`) is what goes into the database. The second (`"Male"`) is what users see in forms and the admin.

**`default`** — value used when none is provided. Must match the stored value if combined with `choices`.

**`null=True`** — allows the database column to store `NULL` (no value at all).

**`blank=True`** — allows the field to be left empty in forms. Without it, Django's form validation requires the field.

```python
phone_number = models.CharField(max_length=10, null=True, blank=True)
# null=True  → database accepts NULL
# blank=True → forms accept an empty input
```

- You usually set both together on optional fields. `null` is a database concern, `blank` is a form concern.

**`unique=True`** — enforces that no two rows can have the same value for this field.

**`auto_now_add=True`** — automatically sets the field to the current timestamp when the record is first created. Never changes after that.

**`auto_now=True`** — automatically updates the field to the current timestamp every time the record is saved.

```python
created_at = models.DateTimeField(auto_now_add=True)  # set once on creation
updated_at = models.DateTimeField(auto_now=True)       # updated on every save
```

**`editable=False`** — hides the field from the Django admin and all model forms.

## Quick Reference

| Field           | Stores             | Common options                         |
| --------------- | ------------------ | -------------------------------------- |
| `CharField`     | Short text         | `max_length` (required)                |
| `EmailField`    | Email address      | validates format automatically         |
| `DateField`     | Date only          | `auto_now`, `auto_now_add`             |
| `DateTimeField` | Date + time        | `auto_now`, `auto_now_add`             |
| `ImageField`    | File path to image | `upload_to`                            |
| `SlugField`     | URL-safe string    | `unique`                               |
| `UUIDField`     | UUID               | `default=uuid.uuid4`, `editable=False` |
