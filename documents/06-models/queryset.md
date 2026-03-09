# QuerySets and Model Instances

## `Product object (1)` — what does that mean?

When you fetch a record from the database, Django gives you back a **model instance** — a Python object representing one row.

If you print it without defining `__str__`, Django shows:

```
Product object (1)
```

Break it down:

```
  Product       object       (1)
    ↑              ↑          ↑
class name    just a label   primary key (id)
```

It tells you the type and which row, but nothing about the actual data inside. That's why `__str__` matters — see [02-str.md](methods/02-str.md).

## What is a QuerySet?

A **QuerySet** is the result of asking Django for records from the database. It is a collection of model instances — like a list, but backed by a database query.

```python
products = Product.objects.all()

print(type(products))
# <class 'django.db.models.query.QuerySet'>

print(products)
# <QuerySet [<Product: Laptop>, <Product: Mouse>]>
```

Every item inside the QuerySet is a model instance — one row from the table.

## A QuerySet is a set of instructions

Before it hits the database, a QuerySet is just a description of what you want — not the data itself.

```python
# This does NOT touch the database.
# Django is holding the instructions: "give me products where price < 100, sorted by name"
qs = Product.objects.filter(price__lt=100).order_by("name")
```

Only when you force it to execute do the instructions become real data:

```python
list(qs)         # execute -> real data
for p in qs:     # execute -> real data
qs[0]            # execute -> real data
qs.count()       # execute -> real data
```

The full lifecycle:

```
.filter().order_by()  ->  instructions (QuerySet)  ->  loop / list / index  ->  real data
```

This is useful — you can keep building and modifying the instructions cheaply, and only pay the database cost once at the end.

## QuerySets are lazy

Django does **not** send a SQL query the moment you write `.filter()` or `.all()`. It waits until you actually use the data. This is called **lazy evaluation**.

```python
# No SQL sent yet
qs = Product.objects.filter(price__lt=100)

# SQL is sent here, when Python needs to loop through the results
for p in qs:
    print(p.name)
```

This means building up a complex query is free — you only pay the database cost when you iterate, convert to a list, or call methods like `.count()`.

## QuerySets are chainable

Each method returns a new QuerySet. You can keep adding conditions and they combine into one SQL query.

```python
Product.objects.filter(price__lt=100).exclude(name="Cable").order_by("name")
```

The original QuerySet is never changed — each chain produces a fresh one.

## Common methods

**Getting all records:**

```python
Product.objects.all()
```

**Filtering — returns a QuerySet:**

```python
Product.objects.filter(price__lt=100)    # price < 100
Product.objects.exclude(name="Cable")    # everything except "Cable"
```

**Getting one record — returns an instance, not a QuerySet:**

```python
Product.objects.get(id=1)      # exactly one match — raises error if 0 or more than 1 found
Product.objects.first()        # first record or None
Product.objects.last()         # last record or None
```

> Use `.get()` only when you are certain exactly one record matches. Use `.filter()` when you expect zero or more.

**QuerySet vs single instance — the difference matters:**

```python
# .filter() always returns a QuerySet, even if only one record matches
products = Product.objects.filter(price=999)
# <QuerySet [<Product: Laptop>]>
products.name       # ✗ error — QuerySet has no .name
products[0].name    # ✓ "Laptop"

# .get() returns the instance directly
product = Product.objects.get(id=1)
# <Product: Laptop>
product.name        # ✓ "Laptop"
```

| Method         | Returns                   | Access fields             |
| -------------- | ------------------------- | ------------------------- |
| `.filter(...)` | QuerySet (0 or more rows) | Must loop or index first  |
| `.all()`       | QuerySet (all rows)       | Must loop or index first  |
| `.get(...)`    | Single instance           | Directly — `product.name` |
| `.first()`     | Single instance or `None` | Directly — `product.name` |

**Ordering:**

```python
Product.objects.order_by("price")    # ascending
Product.objects.order_by("-price")   # descending (note the minus)
```

**Counting:**

```python
Product.objects.count()                     # total rows
Product.objects.filter(price__lt=100).count()   # rows matching a condition
```

**Checking existence:**

```python
Product.objects.filter(name="Laptop").exists()   # True or False — faster than count()
```

## Field lookups

Filters use `__` (double underscore) to express comparisons beyond equality:

```python
Product.objects.filter(price__lt=100)          # price < 100
Product.objects.filter(price__lte=100)         # price <= 100
Product.objects.filter(price__gt=50)           # price > 50
Product.objects.filter(price__gte=50)          # price >= 50
Product.objects.filter(name__contains="pro")   # name contains "pro" (case-sensitive)
Product.objects.filter(name__icontains="pro")  # same, case-insensitive
Product.objects.filter(name__startswith="La")  # name starts with "La"
Product.objects.filter(id__in=[1, 2, 3])       # id is one of these values
```

| Lookup         | SQL equivalent                    |
| -------------- | --------------------------------- |
| `__lt`         | `<`                               |
| `__lte`        | `<=`                              |
| `__gt`         | `>`                               |
| `__gte`        | `>=`                              |
| `__exact`      | `=` (default, same as no lookup)  |
| `__contains`   | `LIKE '%value%'`                  |
| `__icontains`  | `LIKE '%value%'` case-insensitive |
| `__startswith` | `LIKE 'value%'`                   |
| `__in`         | `IN (1, 2, 3)`                    |

## Seeing the SQL Django generates

Useful when learning — print the `.query` attribute:

```python
qs = Product.objects.filter(price__lt=100).order_by("name")
print(qs.query)
# SELECT "products_product"."id", "products_product"."name", ...
# FROM "products_product" WHERE "products_product"."price" < 100
# ORDER BY "products_product"."name" ASC
```
