from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY_CHOICES=(
    ('PZ','Pizza'),
    ('DR','Drinks'),
    ('BR','Burgers'),
    ('PS','Pasta'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField(null=True)
    description = models.TextField()
    composition = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.IntegerField(default=+3706)
    locality = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.name

