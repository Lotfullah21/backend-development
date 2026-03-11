from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    department = models.ForeignKey(Department, models.CASCADE)
    name = models.CharField(max_length=90)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='students')
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name