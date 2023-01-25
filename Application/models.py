
from django.db import models


# Create your models here.
class User(models.Model):
    sNumber=models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField(max_length=30)

    def __str__(self):
        return self.name

