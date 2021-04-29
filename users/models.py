from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

from products.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    karma = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Message(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=True, related_name='receiver', on_delete=models.CASCADE)
    msg_content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Key:{self.pk}, sender:{self.sender}, receiver:{self.receiver}'


class Barter(models.Model):
    status = models.BooleanField(default=False)
    user1 = models.ForeignKey(User, null=True, related_name='user1', on_delete=models.CASCADE)
    product1 = models.ForeignKey(Product, null=True, related_name='product1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, null=True, related_name='user2', on_delete=models.CASCADE)
    product2 = models.ForeignKey(Product, null=True, related_name='product2', on_delete=models.CASCADE)

    def __str__(self):
        return f"status:{self.status}, user1:{self.user1}, product1:{self.product1}, user2:{self.user2}, product2:{self.product2}"
