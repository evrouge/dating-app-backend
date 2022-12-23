from django.db import models

# Create your models here.
class Dating(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    ethnicity = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    hobbies = models.TextField()
    occupation = models.CharField(max_length=32)
    image = models.TextField()
