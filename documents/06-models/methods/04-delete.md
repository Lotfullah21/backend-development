# Overriding `delete()`

Like `save()`, you can override `delete()` to run custom logic before a record is removed from the database. A common use case is cleaning up files stored on disk when a record is deleted.

```python
# models.py
import os
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    file  = models.FileField(upload_to="documents/")

    def delete(self, *args, **kwargs):
        # delete the file from disk before removing the database record
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)
```

When you call `doc.delete()`:

1. Your custom `delete()` checks if the file exists and removes it from disk.
2. `super().delete()` removes the row from the database.

- Always call `super().delete(*args, **kwargs)` — without it the record stays in the database.

## Single delete vs bulk delete

Overriding `delete()` only runs when you delete **one instance at a time**:

```python
doc = Document.objects.get(id=1)
doc.delete()   # custom delete() runs
```

It does **not** run for bulk deletes:

```python
Document.objects.filter(title="old").delete()   # custom delete() is skipped
```

Bulk deletes go straight to SQL and bypass the model entirely. If your custom logic (like deleting files) must always run, delete records one by one in a loop, or use Django signals instead.
