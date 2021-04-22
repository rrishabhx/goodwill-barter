from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a product category (e.g. Electronics)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    product_id = models.CharField(max_length=255)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    photo_id = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, default='product_pics/default-product.jpg',
                              upload_to=f'product_pics')
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=255, default='miscellaneous')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    # def save(self, **kwargs):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save()

# class ProductFollow(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#
# class Barter(models.Model):
#     barter_id = models.CharField(max_length=100)
#     status = models.BooleanField(default=False)
#     user1 = models.ForeignKey()
