# Database Write Operations

This covers how to **create, update, and delete** records using Django's ORM. For reading records (`.filter()`, `.get()`, etc.) see [queryset.md](queryset.md).

## Create

**Option 1 — `create()`:** builds the object and saves it in one step.

```python
product = Product.objects.create(name="Laptop", price=999)
# one line — the row is immediately in the database
```

**Option 2 — instantiate then `save()`:** useful when you need to do something with the object before saving.

```python
product = Product(name="Laptop", price=999)
product.slug = "laptop"   # set extra fields
product.save()            # now it hits the database
```

**Option 3 — `get_or_create()`:** fetches a record if it exists, creates it if it doesn't. Returns a tuple `(instance, created)`.

```python
product, created = Product.objects.get_or_create(
    name="Laptop",
    defaults={"price": 999}
)

if created:
    print("new record was created")
else:
    print("existing record was returned")
```

- `defaults` are only used when creating — they are not used to look up the record.

## Update

**Updating one record** — fetch it, change fields, call `save()`.

```python
product = Product.objects.get(id=1)
product.price = 899
product.save()
```

To update only specific fields (avoids overwriting others accidentally):

```python
product.price = 899
product.save(update_fields=["price"])   # only the price column is written
```

**Bulk update** — update many records in one SQL query without fetching them first.

```python
Product.objects.filter(price__gt=500).update(price=499)
# UPDATE products SET price=499 WHERE price - 500
```

- Bulk `.update()` is faster than looping and saving one by one, but it bypasses the model's `save()` method and any signals attached to it.

**`update_or_create()`** — updates a record if found, creates it if not.

```python
product, created = Product.objects.update_or_create(
    name="Laptop",                  # look up by this
    defaults={"price": 799}         # set/update these fields
)
```

## Delete

**Deleting one record** — fetch it, call `delete()`.

```python
product = Product.objects.get(id=1)
product.delete()
```

**Bulk delete** — delete all records matching a condition in one SQL query.

```python
Product.objects.filter(price__lt=10).delete()
# DELETE FROM products WHERE price < 10
```

- Bulk `.delete()` bypasses each model's `delete()` method override (see [04-delete.md](methods/04-delete.md)). Use it when you don't need custom deletion logic to run per object.

## Quick reference

| Goal                         | Method                                         | Notes                           |
| ---------------------------- | ---------------------------------------------- | ------------------------------- |
| Create one record            | `objects.create(...)`                          | Saves immediately               |
| Create (with pre-save logic) | `instance.save()`                              | Build first, save later         |
| Fetch or create              | `objects.get_or_create(...)`                   | Returns `(obj, created)`        |
| Update one record            | `obj.save()` / `obj.save(update_fields=[...])` | Fetch first                     |
| Bulk update                  | `objects.filter(...).update(...)`              | One SQL query, skips `save()`   |
| Update or create             | `objects.update_or_create(...)`                | Returns `(obj, created)`        |
| Delete one record            | `obj.delete()`                                 | Fetch first                     |
| Bulk delete                  | `objects.filter(...).delete()`                 | One SQL query, skips `delete()` |
