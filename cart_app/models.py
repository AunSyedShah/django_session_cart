from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50, default='')
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    
