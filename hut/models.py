from django.db import models


# Create your models here.
def Huts(models.Model):
    hutname = models.CharField(max_length=128)
    image = models.ImageField()
    altitude = models.IntegerField()
    mountain = models.CharField(max_length=64)
    people_capacity = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()