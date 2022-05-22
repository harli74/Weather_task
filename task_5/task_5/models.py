from django.db import models


# Create your models here.
class Cities(models.Model):
    city_name = models.CharField(max_length=30)
    temperature = models.CharField(max_length=10)
    weather = models.CharField(max_length=50)
    humidity = models.CharField(max_length=30)