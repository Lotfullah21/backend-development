## View

A Django view is a Python callable that receives a `request` and returns a `response`.

## View logic

In Django's `MVT` architecture, the URL dispatcher calls the matching view.

The view then works with:

- the request data coming from the client
- the model layer to read or write data
- the template layer to return HTML

The view is the part that connects these pieces.

## What a view does

- receives the HTTP request
- runs your logic
- reads data from the model if needed
- passes context to a template if needed
- returns `HttpResponse` or `render()`

## Request and response

The request arrives as an `HttpRequest` object.

The view returns an `HttpResponse` object. When you use `render()`, Django builds that response for you.

## Minimal example

```py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django")
```

## GET and POST

Most beginner examples check `request.method` to decide what to do.

```py
from django.http import HttpResponse

def my_view(request):
    if request.method == "GET":
        value = request.GET.get("key")
        return HttpResponse(f"GET value: {value}")

    if request.method == "POST":
        value = request.POST.get("key")
        return HttpResponse(f"POST value: {value}")

    return HttpResponse("Method not supported", status=405)
```

## Common use

- `GET`: usually used to read data
- `POST`: usually used to create or update data

Do not use `GET` for destructive actions in real projects.

## Rendering a template

```py
from django.shortcuts import render

def home(request):
    context = {"title": "Home Page"}
    return render(request, "index.html", context)
```

## Working with models and templates

```py
from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/list.html", {"courses": courses})
```

In this example:

- the view reads data from the model
- the view passes that data to the template
- the template shows it to the user

## URL connection

```py
from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]
```

## Quick rule

If the function or class handles a request and returns a response, it is a view.
