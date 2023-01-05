from django.db import models

# Create your models here.


class Dating(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    hobbies = models.TextField()
    occupation = models.CharField(max_length=32)
    image = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
