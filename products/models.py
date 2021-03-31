from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_id = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_id = models.CharField(max_length=64)
    available = models.BooleanField()
    description = models.TextField()
