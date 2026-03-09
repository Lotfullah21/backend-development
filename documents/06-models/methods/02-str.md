# `__str__()`

`__str__` controls what you see when a model instance is printed or displayed as a string. Without it, Django shows something useless like `Product object (1)`.

```python
# models.py
from django.db import models

class Product(models.Model):
    name  = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
```

In the shell without `__str__`:

```python
p = Product.objects.get(id=1)
print(p)   # -- Product object (1)
```

Add `__str__` to make it readable:

```python
class Product(models.Model):
    name  = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"
```

Now:

```python
p = Product.objects.get(id=1)
print(p)   # -- Laptop ($999.99)
```

- Django's admin panel uses `__str__` to display records in lists and dropdowns. Always define it — it makes debugging and admin navigation much easier.

It also shows up automatically in QuerySets:

```python
products = Product.objects.all()
print(products)
# -- <QuerySet [Laptop ($999.99), Mouse ($29.99)]-
```
