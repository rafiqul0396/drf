from django.db import models



class Students(models.Model):
    name = models.CharField(max_length=120)
    roll=models.IntegerField()
    city=models.CharField(max_length=120)

    


# Create your models here.
