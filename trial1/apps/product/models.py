from django.db import models
from apps.vendor.models import Vendor

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=250)

    def __str__(self):
        return self.title

    



class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    vendor=models.ForeignKey(Vendor,related_name='products',on_delete=models.CASCADE)
    slug=models.SlugField(max_length=250)

    def __str__(self):
        return self.title
