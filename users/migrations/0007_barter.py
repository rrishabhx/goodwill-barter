# Generated by Django 3.1.7 on 2021-04-28 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210421_2027'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20210424_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('product1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='products.product')),
                ('product2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product2', to='products.product')),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]