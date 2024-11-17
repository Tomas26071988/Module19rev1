
from django.db import models

class Buyer(models.Model):
    objects = None
    username = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=128)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

# Create your models here.
