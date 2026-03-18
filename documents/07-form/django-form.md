# Django Forms

Django gives you two ways to handle form submissions:

1. **Django Form / ModelForm** — Django generates the HTML fields for you
2. **Plain HTML form** — you write the HTML yourself and read `request.POST` manually

## 1. Django Form

Create a form class in `forms.py`:

```py
# forms.py
from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(max_length=120)
    age     = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea)
```

Use it in your view:

```py
# views.py
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("/contact/")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
```

Render it in the template:

```html
<!-- contact.html -->
<form method="POST">
	{% csrf_token %} {{ form }}
	<button type="submit">Submit</button>
</form>
```

| Key concept         | What it does                                                              |
| ------------------- | ------------------------------------------------------------------------- |
| `request.POST`      | Dict-like object containing all submitted POST data                       |
| `form.is_valid()`   | Checks all fields pass validation, returns `True`/`False`                 |
| `form.cleaned_data` | Dict of validated data — only available after `is_valid()` returns `True` |
| `redirect()`        | Sends user to a new URL — prevents duplicate submissions on page reload   |

## 2. ModelForm

A **ModelForm** generates form fields directly from a model — no need to define fields twice.

Define a model:

```py
# models.py
class Contact(models.Model):
    name    = models.CharField(max_length=120)
    age     = models.IntegerField()
    comment = models.CharField(max_length=10000)
```

Create a ModelForm from it:

```py
# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model  = Contact
        fields = "__all__"
```

`class Meta` options:

| Option    | What it does                                                                                      |
| --------- | ------------------------------------------------------------------------------------------------- |
| `model`   | The model to generate fields from                                                                 |
| `fields`  | `"__all__"` for all fields, or a list like `["name", "age"]`                                      |
| `exclude` | Fields to skip — but set `null=True, blank=True` on the model field since it won't get form input |

The big advantage — you can call `form.save()` directly:

```py
# views.py
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # creates and saves the model instance
            return redirect("/contact/")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
```

## 3. Plain HTML form

When you need full control over the markup, write the HTML yourself and read `request.POST` manually:

```html
<!-- request_product.html -->
<form method="POST">
	{% csrf_token %}
	<label for="name">Product name</label>
	<input type="text" id="name" name="name" required />

	<label for="quantity">Quantity</label>
	<input type="number" id="quantity" name="quantity" required />

	<button type="submit">Submit</button>
</form>
```

```py
# views.py
def request_product(request):
    if request.method == "POST":
        product_name = request.POST.get("name")
        quantity     = request.POST.get("quantity")
        product = Product(product_name=product_name, quantity=quantity)
        product.save()
        return redirect("/request-product/")
    return render(request, "request_product.html")
```

- The `name` attribute on each `<input>` is the key you use to read it from `request.POST`.

## File uploads

For file uploads, add `enctype="multipart/form-data"` to the form and read files from `request.FILES`:

```html
<form method="POST" enctype="multipart/form-data">
	{% csrf_token %} {{ form }}
	<button type="submit">Submit</button>
</form>
```

| Attribute             | Purpose                                                             |
| --------------------- | ------------------------------------------------------------------- |
| Default `enctype`     | `application/x-www-form-urlencoded` — text data only                |
| `multipart/form-data` | Sends each field as a separate part — required for binary file data |

## Messages framework

Django's messages framework lets you send one-time feedback to the user (success, warning, error):

```py
# views.py
from django.contrib import messages

def request_product(request):
    if request.method == "POST":
        # ... validate and save ...
        messages.success(request, "Product submitted!")
        return redirect("/request-product/")
    return render(request, "request_product.html")
```

Messages are automatically available in templates — no need to pass them in context. Just display them:

```html
{% for message in messages %}
<p>{{ message }}</p>
{% endfor %}
```

## Validation in plain HTML forms

With plain HTML forms, you handle validation yourself in the view:

```py
# views.py
from django.contrib import messages

def request_product(request):
    if request.method == "POST":
        product_name = request.POST.get("name")
        quantity     = request.POST.get("quantity")

        if not product_name:
            messages.warning(request, "Product name is required")
            return redirect("/request-product/")

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            messages.warning(request, "Quantity must be a number")
            return redirect("/request-product/")

        Product(product_name=product_name, quantity=quantity).save()
        messages.success(request, "Product submitted!")
        return redirect("/request-product/")

    return render(request, "request_product.html")
```

- With Django Forms / ModelForms, validation is built in — `form.is_valid()` handles it for you. Manual validation is only needed when using plain HTML forms.
