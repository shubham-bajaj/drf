from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content =models.TextField(blank=True,null=True)
    price = models.DecimalField(default=99.999, max_digits=15, decimal_places=2)
