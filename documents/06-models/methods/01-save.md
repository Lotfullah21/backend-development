# The `save()` Method

Every Django model instance has a `save()` method. Calling it writes the object to the database — either inserting a new row or updating an existing one.

```python
user = User(first_name="John", last_name="Doe")
user.save()   # INSERT — creates a new row

user.first_name = "Jane"
user.save()   # UPDATE — modifies the existing row
```

`User.objects.create(...)` is just shorthand — it calls `save()` internally.

## Overriding `save()`

You can override `save()` inside your model to run custom logic **before** the record is written to the database. A common use case is auto-generating a slug from a name.

```python
# models.py
from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    product_name = models.CharField(max_length=120)
    slug         = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)   # generate slug before saving
        super().save(*args, **kwargs)             # call Django's original save()
```

When you call `product.save()`:

1. Your custom `save()` runs first — it generates the slug.
2. `super().save()` runs next — it does the actual database write.

## `slugify`

`slugify` converts a string into a URL-safe format:

```python
slugify("Hello World!")   # -> "hello-world"
slugify("Django & REST")  # -> "django-rest"
```

It lowercases the string, replaces spaces with hyphens, and removes any characters that aren't letters, numbers, or hyphens.

## `super().save(*args, **kwargs)`

`super()` refers to the parent class — in this case `models.Model`. Calling `super().save()` hands control back to Django's original save logic, which is what actually writes to the database.

The `*args` and `**kwargs` are passed through so that any options given to your save call (like `update_fields`) are forwarded correctly:

```python
product.save(update_fields=["slug"])   # this kwarg needs to reach Django's save()
```

## What happens if you forget `super()`

If you override `save()` but don't call `super().save()`, **nothing gets written to the database**. Your custom logic runs but Django never executes the SQL.

```python
def save(self, *args, **kwargs):
    self.slug = slugify(self.product_name)
    # super().save() missing — the record is never saved
```

Always call `super().save(*args, **kwargs)` at the end of an overridden `save()`.
