- ## Install the package

```py
pip install django-ckeditor
```

- Add 'ckeditor' to INSTALLED_APPS in settings.py.
- Update Course model's description field:

```py
from ckeditor.fields import RichTextField
class Subject(models.Model):
    title = models.CharField(max_length=132, unique=True)
    description = RichTextField(blank=True, null=True)

```

- enable formatting in settings.py

```py
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': 'codesnippet',  # Enable the code snippet plugin
        'height': 300,
        'width': 'auto',
    },
}

```

```py

- This is some text explaining the code.

<code>
def example_function():
    return "Hello, World!"
</code>

Here is more text describing what the code does.

```

## Sanitize HTML Content

To prevent malicious scripts, sanitize the HTML content before saving it to the database. Use libraries like Bleach for this.

```sh
pip install bleach
```

```py
serializers.py
import bleach

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        allowed_tags = ['p', 'b', 'i', 'u', 'a', 'ul', 'ol', 'li', 'br', 'code', 'pre']
        allowed_attrs = {'a': ['href', 'title']}
        representation['description'] = bleach.clean(
            representation['description'], tags=allowed_tags, attributes=allowed_attrs
        )
        return representation
```
