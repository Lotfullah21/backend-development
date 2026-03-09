# Python Packages and `__init__.py`

## What is a Python package?

A **package** is a directory that contains Python modules (`.py` files). Packages let you organize code into namespaces so you can group related logic together and import it cleanly.

```text
mypackage/
├─ __init__.py
├─ module_a.py
└─ module_b.py
```

## What makes a directory a package?

There are two kinds of packages in Python:

**Regular package** — has an `__init__.py` file. This was the only way before Python 3.3.

**Namespace package** (Python 3.3+) — a directory *without* `__init__.py` that Python can still import from. This is why you can write `from students import views` even if `students/` has no `__init__.py` — Python 3.3+ treats it as a namespace package automatically.

```text
blog/              <- namespace package (Python 3.3+): importable, no __init__.py needed
blog/__init__.py   <- regular package: explicitly marked, works in all Python versions
```

## What does `__init__.py` do?

1. **Marks the directory as a package** — Python recognizes it as importable
2. **Runs on import** — any code inside it executes the first time the package is imported
3. **Controls the public API** — you can re-export names to make imports cleaner

```python
# mypackage/__init__.py

from .module_a import SomeClass   # re-export for convenience
__all__ = ["SomeClass"]           # controls what `from mypackage import *` exposes
```

Then anywhere in your project:

```python
from mypackage import SomeClass        # clean import via __init__.py
from mypackage.module_b import helper  # direct module access also works
```

## Why this matters in Django

Every time `startproject` or `startapp` runs, Django creates `__init__.py` files automatically. This is what makes your project and apps importable as Python packages.

```text
mysite/
├─ manage.py
└─ mysite/
   ├─ __init__.py   <- makes mysite/ a package
   ├─ settings.py
   ├─ urls.py
   └─ wsgi.py

blog/
├─ __init__.py      <- makes blog/ a package
├─ models.py
├─ views.py
└─ migrations/
   └─ __init__.py   <- makes migrations/ a package too
```

Because of these files, Django (and you) can write imports like:

```python
from blog.models import Post
from blog.views import post_list
from mysite.settings import BASE_DIR
```

Since Django runs on Python 3.3+, most of these imports would also work without `__init__.py` thanks to namespace packages. But Django still generates them as a convention for one clear reason:

- **Explicitness** — `__init__.py` makes intent clear: this directory is meant to be a Python package, not just a folder that happens to contain `.py` files. It also ensures compatibility regardless of how Django's internals evolve across versions.

## Empty vs non-empty `__init__.py`

In most Django apps the file is left **empty** — its only job is to mark the directory as a package. You only add code to it when you want to re-export names or run initialization logic at the package level.

| `__init__.py` content           | Effect                                       |
| ------------------------------- | -------------------------------------------- |
| Empty                           | Marks directory as a package, nothing else   |
| Re-exports (`from .x import Y`) | Shortcuts for cleaner imports elsewhere      |
| Setup code                      | Runs once when the package is first imported |

## Regular package vs namespace package — summary

| | Regular package | Namespace package |
| --- | --- | --- |
| Requires `__init__.py` | Yes | No |
| Python version | All versions | 3.3+ |
| Importable in Django | Yes | Yes (Python 3.3+) |
| Best practice in Django | Yes | Avoid — keep what Django generates |

**Rule of thumb:** keep the `__init__.py` files Django generates. They are not always strictly required in Python 3.3+, but they are the convention Django follows and removing them is unnecessary.
