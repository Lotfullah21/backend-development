## bulk_create()

bulk_create is a method provided by Django's ORM (Object-Relational Mapping) that allows us to insert multiple records into the database at once, rather than making individual INSERT queries for each object.

This significantly improves performance when dealing with a large number of records because it reduces the number of database queries.

### How bulk_create Works:

Instead of calling save() for each object (which would send one query per object to the database), bulk_create sends a single query to insert multiple objects in a single database transaction.
It doesn't trigger signals like pre_save, post_save, or full_clean for each individual object, which makes it faster but less flexible in terms of handling object-specific logic.

### Key Points:

`No Many-to-Many Relationships`: You cannot set many-to-many fields (like skills.add() in your case) during bulk_create. These relationships must be added later because the objects aren't saved to the database until bulk_create completes.
`No Signals`: Django’s model signals (pre_save, post_save, etc.) do not get triggered with bulk_create.

## Meta classes

a Meta class is an inner class that provides metadata for the model. It is used to define options that affect the behavior of the model, such as database table name, ordering, and constraints, among others.

## Common Meta options

### 1. `db_table`:

- it defines the name of the database table for the model
- if name is not specified here, Django generates a table name based on the app and table name.

```py
class College(models.Model):
    college_name = models.CharField(max_length=100)
    def __str__(self):
        return self.college_name
    class Meta:
        db_table="custom_college_table_for_students"
```

### 2. `ordering`:

Defines the default order in which objects are retrieved when querying the database.

```py

class Meta:
    ordering = ['college_name']  # Orders by the 'name' field
```

### 3. `verbose_name and verbose_name_plural`:

Defines human-readable singular and plural names for the model in Django's admin.

```py
class Meta:
    verbose_name = 'Student'
    verbose_name_plural = 'Students'

```

### 4. `constraints`:

Allows defining complex constraints like UniqueConstraint, CheckConstraint.

##### 1. `UniqueConstraint`: This constraint ensures that the combination of values in specified fields is unique across all rows in the table.

```py
from django.db import models

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course')
        ]

```

In this case, no two rows in the Enrollment table can have the same combination of student and course.

### Key attributes:

fields: Specifies the fields that should be unique together.
name: The name of the constraint, which is necessary to identify the constraint and helpful when modifying or removing it later.

##### 5. `CheckConstraint`

This constraint enforces a condition that must be true for every row in the database. It ensures that specific logical conditions are met before a row can be saved.

```py
from django.db import models
from django.db.models import Q

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(age__gte=18), name='age_at_least_18')
        ]

```

The CheckConstraint ensures that every student must be at least 18 years old (age\_\_gte=18)

Combining multiple constraints

```py
from django.db import models
from django.db.models import Q

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course'),
            models.CheckConstraint(check=Q(student__age__gte=18), name='student_age_at_least_18')
        ]

```

#### Key attributes:

check: A Q object that specifies the condition that must be true.
name: A name for the constraint

### 6. abstract:

If set to True, the model becomes abstract, meaning Django won’t create a database table for it. Instead, it is used as a base class for other models.

```py
class BaseModel(models.Model):
    college_name = models.CharField(max_length=100)
    def __str__(self):
        return self.college_name
    class Meta:
        abstract = True

```

Now, for base model, we are not going to create a new table, instead it might be used in some other models.

For instance, in some of the model, we need created_at, updated_at, we can create a base model and define these custom fields inside, and also add the `abstract=True` for `Meta` class.

BaseModel is an abstract model that extends models.Model.

```py
class BaseModel(models.Model):
    field_from_base_model = models.CharField(max_length=102, default="BASE FIELD")

    class Meta:
        abstract = True

    def __str__(self):
        return self.field_from_base_model


class Product(BaseModel):
    product_name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.product_name}")
        super(Product, self).save(*args, **kwargs)


class College(BaseModel):
    college_name = models.CharField(max_length=100)
    def __str__(self):
        return self.college_name

class Department(BaseModel):
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name
```

Now, all models that uses `BaseModel` as their parent will have an extra field `field_from_base_model`.

### 7. indexes:

Ensures that a combination of fields is indexed together, which can improve query performance.
This can significantly improve query performance when those fields are used together in lookups, particularly in complex queries involving filtering, sorting, or joining multiple fields.

Indexes help the database quickly locate rows without scanning the entire table. When fields are often queried together (e.g., in a WHERE or ORDER BY clause), creating a composite index (i.e., an index on multiple fields) can speed up these operations.

Syntax:

```py
class Meta:
    indexes = (('field1', 'field2'),)
```

Suppose you have a Book model where you frequently query books by both author and published_date:

```py
from django.db.models import Index

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        indexes = [
            Index(fields=['author', 'published_date'], name='author_pubdate_idx'),
        ]

```
