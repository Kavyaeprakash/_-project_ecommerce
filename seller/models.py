from django.db import models
from common.models import Seller

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50)
    product_no = models.BigIntegerField()
    product_stock = models.IntegerField()
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to = 'product/')
    
    class Meta:
        db_table = 'product_tb'