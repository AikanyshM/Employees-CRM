from tkinter import CASCADE
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class Employee(models.Model):
    first_last_name = models.CharField(max_length=250)
    birthdate = models.DateField()
    employment_date = models.DateField()
    position = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_last_name

