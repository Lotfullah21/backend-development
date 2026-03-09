## HttpResponse

You are responsible for building and returning an `HttpResponse` from every view. Django sends it back to the browser.

### Basic response

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world!")
```

### Setting the status code

```python
return HttpResponse("Not found", status=404)
return HttpResponse("Created",   status=201)
```

### Setting content type

```python
return HttpResponse("<h1>Hello</h1>", content_type="text/html")
return HttpResponse('{"ok": true}',   content_type="application/json")
```

### Setting response headers

```python
response = HttpResponse("ok")
response["X-Custom-Header"] = "my-value"
return response
```

## Common response shortcuts

Django provides helpers so you don't have to build every response manually.

### `render()` — return an HTML template

```python
from django.shortcuts import render

def book_list(request):
    books = Book.objects.all()
    return render(request, "books/list.html", {"books": books})
    #              ↑ request   ↑ template path    ↑ context dict
```

The context dict is what your template can access. Every key becomes a template variable.

### `JsonResponse` — return JSON

```python
from django.http import JsonResponse

def api_books(request):
    return JsonResponse({"books": ["Django", "Python"]})
    # automatically sets Content-Type: application/json
```

For a list at the top level, pass `safe=False`:

```python
return JsonResponse([1, 2, 3], safe=False)
```

### `redirect()` — send the browser to another URL

```python
from django.shortcuts import redirect

def old_page(request):
    return redirect("/new-url/")          # by path string

def save_and_go(request):
    return redirect("book-list")          # by named URL
```

`redirect()` returns a 302 by default. Pass `permanent=True` for a 301.

## Named response classes

Django has specific subclasses for common responses instead of always setting `status=` manually:

| Class                           | Status | Use                |
| ------------------------------- | ------ | ------------------ |
| `HttpResponse`                  | 200    | Default            |
| `HttpResponseRedirect`          | 302    | Redirect           |
| `HttpResponsePermanentRedirect` | 301    | Permanent redirect |
| `HttpResponseNotFound`          | 404    | Not found          |
| `HttpResponseForbidden`         | 403    | No permission      |
| `HttpResponseBadRequest`        | 400    | Bad input          |
| `HttpResponseServerError`       | 500    | Server error       |

```python
from django.http import HttpResponseNotFound

def get_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponseNotFound("No book with that ID")
    return HttpResponse(book.title)
```

Or use the shortcut `get_object_or_404()` which does the same thing in one line:

```python
from django.shortcuts import get_object_or_404

def get_book(request, id):
    book = get_object_or_404(Book, id=id)   # raises 404 if not found
    return HttpResponse(book.title)
```

## Quick reference

| You want to...         | Use                                                           |
| ---------------------- | ------------------------------------------------------------- |
| Check request method   | `request.method`                                              |
| Read a query param     | `request.GET.get("key", default)`                             |
| Read a form field      | `request.POST.get("key", default)`                            |
| Read JSON body         | `json.loads(request.body)`                                    |
| Read a header          | `request.headers.get("Name")`                                 |
| Check who is logged in | `request.user` / `request.user.is_authenticated`              |
| Return HTML            | `render(request, "template.html", context)`                   |
| Return JSON            | `JsonResponse({"key": "value"})`                              |
| Redirect               | `redirect("url-name")` or `redirect("/path/")`                |
| Return a 404           | `HttpResponseNotFound()` or `get_object_or_404(Model, id=id)` |
