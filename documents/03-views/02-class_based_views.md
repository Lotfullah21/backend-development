## Class Based View

A Class-Based View (`CBV`) is a Python class used as a Django view.

## Best use

- repeated patterns
- larger views
- reusable logic
- Django generic views

## Basic example

```py
from django.http import HttpResponse
from django.views import View

class CourseListView(View):
    def get(self, request):
        return HttpResponse("All courses")
```

## Example with `GET` and `POST`

```py
from django.http import HttpResponse
from django.views import View

class ContactView(View):
    def get(self, request):
        return HttpResponse("Contact form page")

    def post(self, request):
        return HttpResponse("Form submitted")
```

Each HTTP method lives in its own method like `get()` and `post()`, which makes the code easier to organize than a long chain of `if request.method == ...`.

## URL connection

```py
from django.urls import path
from .views import CourseListView

urlpatterns = [
    path("courses/", CourseListView.as_view(), name="course_list"),
]
```

## Generic views

Django also provides generic class-based views for common tasks.

Examples:

- `TemplateView`
- `ListView`
- `DetailView`
- `CreateView`
- `UpdateView`

These are useful when Django can handle most of the repeated work for you.

## Generic view example

```py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"
```

## Strength

Logic is split into methods like `get()` and `post()`, and code is easier to reuse.

## Weakness

It is less obvious at first and requires understanding `.as_view()` and class inheritance.
