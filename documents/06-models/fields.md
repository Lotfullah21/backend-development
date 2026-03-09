# Django Model Fields

Every field in a model maps to a **column** in the database. You pick the field type based on what kind of data the column stores.

## Text fields

```python
# Short text — always requires max_length
name = models.CharField(max_length=100)

# Long text — no max_length needed
bio = models.TextField()

# URL-friendly text (letters, numbers, hyphens)
slug = models.SlugField(unique=True)   # max_length=50 by default

# Email with built-in validation
email = models.EmailField()            # max_length=254 by default

# URL with validation
website = models.URLField()            # max_length=200 by default
```

## Number fields

```python
# Integer (-2B to +2B)
age = models.IntegerField()

# Only positive integers (0 and above)
price = models.PositiveIntegerField()

# Small integer (-32768 to 32767)
quantity = models.SmallIntegerField()

# Large integer (beyond 2B)
population = models.BigIntegerField()

# Decimal — exact precision (use for money)
price = models.DecimalField(max_digits=10, decimal_places=2)   # 99999999.99

# Float — approximate (use for scientific values, not money)
rating = models.FloatField()
```

- Use `DecimalField` for money, not `FloatField`. Floats have rounding errors (`0.1 + 0.2 = 0.30000000000000004`).

## Boolean

```python
is_active = models.BooleanField(default=True)
```

## Date and time fields

```python
# Date only (YYYY-MM-DD)
date_of_birth = models.DateField()

# Date + time
created_at = models.DateTimeField()

# Time only (HH:MM:SS)
alarm_time = models.TimeField()

# Duration (timedelta)
duration = models.DurationField()
```

**Auto-timestamps** — the most common pattern:

```python
# Set once when the record is first created
created_at = models.DateTimeField(auto_now_add=True)

# Updated every time the record is saved
updated_at = models.DateTimeField(auto_now=True)
```

## File and image fields

```python
# Any file
document = models.FileField(upload_to="documents/")

# Image (requires Pillow: pip install Pillow)
avatar = models.ImageField(upload_to="avatars/")
```

`upload_to` sets the subdirectory inside your `MEDIA_ROOT`.

## ID / Primary key fields

```python
# Default — Django adds this automatically
id = models.AutoField(primary_key=True)           # 1, 2, 3, ...
id = models.BigAutoField(primary_key=True)         # same but bigger range

# UUID — non-guessable, good for public APIs
import uuid
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```

## JSON field

```python
# Store structured data (dict, list) — works on PostgreSQL, MySQL 5.7+, SQLite 3.9+
metadata = models.JSONField(default=dict)
```

## Common field options

These options work on **any** field type:

```python
name = models.CharField(
    max_length=100,
    null=True,          # allows NULL in the database
    blank=True,         # allows empty string in forms/validation
    default="Unknown",  # default value if none is provided
    unique=True,        # no two rows can have the same value
    db_index=True,      # creates a database index (faster lookups)
    choices=[           # restricts to a fixed set of values
        ("draft", "Draft"),
        ("published", "Published"),
    ],
    help_text="Enter the name",   # shown in admin/forms
    verbose_name="Full Name",     # human-readable label
    editable=False,     # hidden from forms, cannot be set by user
)
```

### `null` vs `blank`

|        | `null=True`                                         | `blank=True`                 |
| ------ | --------------------------------------------------- | ---------------------------- |
| Where  | Database level                                      | Validation / form level      |
| Means  | Column allows `NULL`                                | Field can be submitted empty |
| Use on | Non-text fields (`IntegerField`, `DateField`, etc.) | Any field                    |

- Avoid `null=True` on text fields (`CharField`, `TextField`). Use `blank=True, default=""` instead — otherwise you have two ways to represent "empty" (`NULL` and `""`).

### `choices` — limiting values

```python
class Article(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
```

```python
article = Article.objects.create(title="Hello", status="draft")
article.get_status_display()   # "Draft" — human-readable label
```

## Quick reference

| Field                  | Stores              | Required args                  |
| ---------------------- | ------------------- | ------------------------------ |
| `CharField`            | Short text          | `max_length`                   |
| `TextField`            | Long text           | —                              |
| `SlugField`            | URL slug            | —                              |
| `EmailField`           | Email               | —                              |
| `IntegerField`         | Integer             | —                              |
| `PositiveIntegerField` | 0+ integer          | —                              |
| `DecimalField`         | Exact decimal       | `max_digits`, `decimal_places` |
| `FloatField`           | Approximate decimal | —                              |
| `BooleanField`         | True / False        | —                              |
| `DateField`            | Date                | —                              |
| `DateTimeField`        | Date + time         | —                              |
| `FileField`            | File upload         | —                              |
| `ImageField`           | Image upload        | —                              |
| `UUIDField`            | UUID                | —                              |
| `JSONField`            | JSON data           | —                              |
| `AutoField`            | Auto-increment ID   | —                              |
