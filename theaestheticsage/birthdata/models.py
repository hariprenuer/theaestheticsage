from django.db import models

# Create your models here.

class Birthdata(models.Model):
    latitude=models.DecimalField(max_digits=12,decimal_places=7)
    longitude=models.DecimalField(max_digits=12,decimal_places=7)
    date=models.IntegerField()
    month=models.IntegerField()
    year=models.IntegerField()
    hour=models.IntegerField()
    minutes=models.IntegerField()