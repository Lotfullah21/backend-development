# `clean()`

`clean()` is where you put **model-level validation** — rules that involve more than one field, or logic that doesn't fit neatly into a single field's definition.

```python
# models.py
from django.core.exceptions import ValidationError
from django.db import models

class Event(models.Model):
    name       = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date   = models.DateField()

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date.")
```

When `clean()` raises `ValidationError`, Django stops and surfaces the error — the record is not saved.

## How `clean()` gets called

`clean()` does **not** run automatically when you call `save()`. It runs when:

- A `ModelForm` is submitted and validated (Django calls it for you).
- You call `full_clean()` manually.

```python
event = Event(name="Conference", start_date="2026-05-10", end_date="2026-05-01")
event.full_clean()   # raises ValidationError: "End date cannot be before start date."
event.save()         # this line is never reached
```

- If you want validation to run on every save, call `full_clean()` inside your `save()` override — but this is usually unnecessary since forms handle it.

## `clean()` vs field-level validation

|               | `clean()`          | Field validators       |
| ------------- | ------------------ | ---------------------- |
| Where defined | Inside the model   | On the field itself    |
| Access to     | All fields at once | One field only         |
| Use for       | Cross-field rules  | Single-field rules     |
| Example       | end - start        | value must be positive |

```python
# field-level validator — only sees one value
from django.core.validators import MinValueValidator

price = models.DecimalField(validators=[MinValueValidator(0)])

# clean() — can compare two fields
def clean(self):
    if self.sale_price - = self.original_price:
        raise ValidationError("Sale price must be less than original price.")
```
