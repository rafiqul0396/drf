from django.db import models




class Products(models.Model):
    title=models.CharField(max_length=120)
    contents=models.TextField(blank=True,null=True)
    price= models.DecimalField( max_digits=5, decimal_places=2,default=99.99)



# Create your models here.
