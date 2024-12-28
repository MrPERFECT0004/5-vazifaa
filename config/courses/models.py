from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Matematika")
    description = models.TextField(verbose_name="Ishonchli")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="10.10.2024")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="10.11.2024")

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Laziz")
    email = models.EmailField(unique=True, verbose_name="yuq")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="15.10.2024")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students", verbose_name="Matematika")

    def __str__(self):
        return self.name
