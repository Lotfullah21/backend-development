## Now, let's move closer to production environment

Let's clear all previous data, we can do this by using shell env in python.

```py
from courses.models import Course, Module, Lesson, Content, Subject
Course.objects.all().delete()
Module.objects.all().delete()
Lesson.objects.all().delete()
Content.objects.all().delete()
```
