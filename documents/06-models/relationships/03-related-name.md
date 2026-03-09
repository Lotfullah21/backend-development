# `related_name` and Reverse Relationships

When you create a ForeignKey, OneToOneField, or ManyToManyField, Django sets up **two directions** of access automatically:

- **Forward** — from the model that has the field (fk,1:N,M:N), to the related model.
- **Reverse** — from the related model, back to the model that has the field.

## Forward access (always works the same)

Access the related object directly through the field name:

```python
# Student has: department = ForeignKey(Department, ...)
student = Student.objects.get(name="Ali")
print(student.department.name)   # "Computer Science"
```

## Reverse access (default: `_set`)

From the parent side, Django creates a reverse accessor automatically. By default it uses `childmodelname_set`:

```python
# Department -> Students (default reverse name)
dept = Department.objects.get(name="Computer Science")
dept.student_set.all()
# <QuerySet [<Student: Ali>, <Student: Sara>, <Student: John>]>
```

The pattern is always `lowercase_modelname_set`.

## How the default name is derived

Django takes the **model class name**, converts it to lowercase, and uses that as the accessor name — with `_set` appended for ForeignKey and ManyToManyField, and nothing appended for OneToOneField.

```
Model class name   ->   Default reverse accessor
─────────────────────────────────────────────────
Student            ->   department.student_set
UserProfile        ->   user.userprofile         ← no _set, no underscore
Profile            ->   user.profile
```

This is why naming matters. If your model is called `UserProfile`, the accessor is `user.userprofile` — not `user.profile`, not `user.user_profile`. Django derives it mechanically from the class name.

```python
# Your model is named UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# In the shell:
user.profile       # AttributeError — no such accessor
user.userprofile   # Works — Django used lowercase("UserProfile")
```

If you want `user.profile`, either rename the class to `Profile`, or set `related_name="profile"` on the field.

## `related_name` — customize the reverse accessor

If `student_set` feels unclear, you can name it yourself with `related_name`:

```python
class Student(models.Model):
    name       = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="students")
```

Now the reverse accessor is `students` instead of `student_set`:

```python
dept = Department.objects.get(name="Computer Science")
dept.students.all()   # cleaner than dept.student_set.all()
```

## How it works with each relationship type

**ForeignKey (one-to-many):**

```python
department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="students")

# forward:  student.department
# reverse:  department.students.all()
```

**OneToOneField (one-to-one):**

```python
user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

# forward:  profile.user
# reverse:  user.profile          ← no .all() because there is only one
```

**ManyToManyField:**

```python
courses = models.ManyToManyField(Course, related_name="students")

# forward:  student.courses.all()
# reverse:  course.students.all()
```

## When `related_name` is required

If two fields on the same model point to the same parent, Django cannot create two reverse accessors with the same default name. You **must** set `related_name` to disambiguate:

```python
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles_written")
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles_edited")
```

Without `related_name` here, Django would try to create `user.article_set` for both fields and raise an error.

## Quick reference

| Relationship    | Default reverse name                                 | With `related_name="students"` |
| --------------- | ---------------------------------------------------- | ------------------------------ |
| ForeignKey      | `department.student_set.all()`                       | `department.students.all()`    |
| OneToOneField   | `user.userprofile` (lowercase class name, no `_set`) | `user.profile`                 |
| ManyToManyField | `course.student_set.all()`                           | `course.students.all()`        |
