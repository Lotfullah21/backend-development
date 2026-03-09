# `get_absolute_url()`

`get_absolute_url` is a Django convention — a method you define on a model that returns the URL for viewing that specific instance. Django itself doesn't call it automatically, but many parts of Django expect it to exist: the admin "View on site" button, `redirect(obj)`, and template tags.

```python
# models.py
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("articles/<slug:slug>/", views.article_detail, name="article-detail"),
]
```

Now you can use it anywhere:

**In a view:**

```python
from django.shortcuts import redirect

def create_article(request):
    article = Article.objects.create(title="Hello", slug="hello")
    return redirect(article)   # Django calls get_absolute_url() automatically
```

**In a template:**

```html
<a href="{{ article.get_absolute_url }}">Read more</a>
```

- Use `reverse()` inside `get_absolute_url` rather than hardcoding the path. If the URL pattern ever changes, you only update `urls.py` — everything else still works.
