from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a product category (e.g. Electronics)')

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    photo_id = models.CharField(max_length=64)
    available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name

# class ProductFollow(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#
# class Barter(models.Model):
#     barter_id = models.CharField(max_length=100)
#     status = models.BooleanField(default=False)
#     user1 = models.ForeignKey()
