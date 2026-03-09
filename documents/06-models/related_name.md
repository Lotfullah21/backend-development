### What is related_name?

When you create a ForeignKey in Django, it automatically sets up two relationships:

` Forward Relationship`: From the child model (e.g., Student) to the parent model (e.g., Course).
`Reverse Relationship`: From the parent model (e.g., Course) to the child model (e.g., Student).

```py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    # establishing many-to-many relationship
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name

```

## Forward and Reverse Relationships

#### Forward Relationship

You can access the CourseCategory from a Course object directly:

```py
student = Student.objects.first()
  # this gives the related CourseCategory object
print(student.courses)
```

#### Reverse Relationship

The `related_name="students"` allows you to access all courses related to a category:

```py
course = Course.objects.first()
 # this fetches all Course objects linked to this category
print(course.courses.all())
```

#### Without related_name

If you don’t set related_name, Django uses a default name for the reverse relationship. By default, it adds \_set to the lowercase child model name.

```py
class Student(models.Model):
    courses = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

```

```py
course = Course.objects.first()
 # default reverse relationship name
print(course.student_set.all())

```

related_name customizes how you access related objects in the reverse direction (parent → child).
