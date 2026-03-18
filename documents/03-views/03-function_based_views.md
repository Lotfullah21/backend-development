## Function Based View

A Function-Based View (`FBV`) is a normal Python function used as a Django view.

## Best use

- small and clear logic
- beginner-friendly code
- custom request handling

## Example

```py
from django.http import HttpResponse

def course_list(request):
    return HttpResponse("All courses")
```

## Example with `GET` and `POST`

```py
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        return HttpResponse("Form submitted")
    return HttpResponse("Contact form page")
```

## Example with request data

```py
from django.http import HttpResponse

def my_view(request):
    if request.method == "GET":
        value = request.GET.get("key")
        return HttpResponse(f"GET value: {value}")

    if request.method == "POST":
        value = request.POST.get("key")
        return HttpResponse(f"POST value: {value}")

    return HttpResponse("Method not allowed", status=405)
```

## Why beginners start here

Function-based views are explicit.

You can see:

- the request object
- the method checks
- the logic
- the response

all in one place.

## URL connection

```py
from django.urls import path
from .views import course_list

urlpatterns = [
    path("courses/", course_list, name="course_list"),
]
```

## Strength

Everything is explicit in one place.

## Weakness

As logic grows, the function can become long and repetitive.
