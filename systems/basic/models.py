from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)




    def __str__(self):
        return self.name