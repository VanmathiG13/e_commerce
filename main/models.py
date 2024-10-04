
from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True,default=1)
    category_name = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image_url = models.URLField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_count = models.IntegerField()
    description = models.TextField(blank=True, null=True)  # Allow null for existing records

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product_name
