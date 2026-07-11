from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name